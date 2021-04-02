import datetime
import logging

import discord
from discord.ext import tasks

from appc.appc_price_repository import AppcPriceRepository
from bot.template_messages import TemplateMessages


class DiscordTasksManager:
    BACKOFF_PERIOD_SECONDS = 60 * 60 * 12  # 12 hours

    def __init__(
        self,
        notification_channel_id: int,
        appc_price_repository: AppcPriceRepository,
        logger: logging.Logger = logging.getLogger("DiscordTasksManager"),
    ):
        self.__notification_channel_id = notification_channel_id
        self.__appc_price_repository = appc_price_repository
        self.__last_message_datetime = None
        self.__channel = None
        self.__logger = logger

    def start(self, client: discord.Client):
        self.__logger.info("Starting DiscordTasksManager...")
        self.__channel = client.get_channel(self.__notification_channel_id)
        self.check_price_change.start()

    @tasks.loop(minutes=5)
    async def check_price_change(self):
        self.__logger.info("Running DiscordClientWrapper.check_price_change.")
        now = datetime.datetime.now()
        if self.__last_message_datetime is not None:
            interval = (now - self.__last_message_datetime).total_seconds()
            if interval < self.BACKOFF_PERIOD_SECONDS:
                return

        stats = self.__appc_price_repository.get_last_24h_stats()
        if stats is None:
            self.__logger.warning("Failed to get current APPC stats.")
            return

        price_usd = self.__appc_price_repository.get_last_price("USD")
        price_eur = self.__appc_price_repository.get_last_price("EUR")
        percentage = stats.get_formatted_price_change()
        self.__logger.info(f"Got: {stats}")

        if stats.price_change_percent >= 20:
            self.__logger.info("Increased more than 20%, sending message")
            self.__last_message_datetime = now
            await self.__channel.send(
                TemplateMessages.get_increase_message(price_usd, price_eur, percentage)
            )
        elif stats.price_change_percent <= -10:
            self.__logger.info("Decreased more than 10%, sending message")
            self.__last_message_datetime = now
            await self.__channel.send(
                TemplateMessages.get_decrease_message(price_usd, price_eur, percentage)
            )
