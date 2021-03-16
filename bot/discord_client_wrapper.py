import datetime
import logging

import discord
from discord.ext import tasks

from appc.appc_price_repository import AppcPriceRepository
from bot.template_messages import TemplateMessages


class DiscordClientWrapper(discord.Client):
    BACKOFF_PERIOD_SECONDS = 60 * 60 * 12  # 12 hours

    def __init__(
        self,
        appc_price_repository: AppcPriceRepository,
        discord_token: str,
        notification_channel_id: int,
        logger: logging.Logger = logging.getLogger("DiscordClientWrapper"),
        **options,
    ):
        super().__init__(**options)
        self.__appc_price_repository = appc_price_repository
        self.__logger = logger
        self.__notification_channel_id = notification_channel_id
        self.__last_message_datetime = datetime.datetime.now()
        self.__start(discord_token)

    def __start(self, discord_token: str):
        self.__logger.info("Starting DiscordClientWrapper...")
        self.run(discord_token)

    async def on_ready(self):
        self.__logger.info(f"{self.user} has connected to Discord!")
        self.check_price_change.start()

    async def on_message(self, message):
        self.__logger.info(f"Received a new message: {message}")
        if message.author == self.user:
            return

        if message.content == "!price":
            price_usd = self.__appc_price_repository.get_last_price("USD")
            price_eur = self.__appc_price_repository.get_last_price("EUR")
            stats = self.__appc_price_repository.get_last_24h_stats()
            percentage = stats.get_formatted_price_change()
            if None in [price_usd, price_eur, percentage]:
                await message.channel.send(TemplateMessages.get_failure_message())
            else:
                await message.channel.send(
                    TemplateMessages.get_price_message(price_usd, price_eur, percentage)
                )
        elif message.content == "!ping":
            await message.channel.send(TemplateMessages.get_ping_message())

    @tasks.loop(minutes=5)
    async def check_price_change(self):
        self.__logger.info("Running DiscordClientWrapper.check_price_change.")
        now = datetime.datetime.now()
        interval = (now - self.__last_message_datetime).total_seconds()
        if interval < self.BACKOFF_PERIOD_SECONDS:
            return

        stats = self.__appc_price_repository.get_last_24h_stats()
        percentage = stats.get_formatted_price_change()
        self.__logger.info(f"Got: {stats}")

        channel = self.get_channel(self.__notification_channel_id)
        if stats.price_change_percent >= 30:
            self.__logger.info("Increased more than 30%, sending message")
            self.__last_message_datetime = now
            await channel.send(TemplateMessages.get_increase_message(percentage))
        elif stats.price_change_percent <= -10:
            self.__logger.info("Decreased more than 10%, sending message")
            self.__last_message_datetime = now
            await channel.send(TemplateMessages.get_decrease_message(percentage))
