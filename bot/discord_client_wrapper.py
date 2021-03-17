import logging

import discord

from appc.appc_price_repository import AppcPriceRepository
from bot.discord_tasks_manager import DiscordTasksManager
from bot.template_messages import TemplateMessages


class DiscordClientWrapper(discord.Client):
    def __init__(
        self,
        appc_price_repository: AppcPriceRepository,
        discord_token: str,
        discord_tasks_manager: DiscordTasksManager,
        logger: logging.Logger = logging.getLogger("DiscordClientWrapper"),
        **options,
    ):
        super().__init__(**options)
        self.__appc_price_repository = appc_price_repository
        self.__discord_token = discord_token
        self.__discord_tasks_manager = discord_tasks_manager
        self.__logger = logger

    def start_client(self):
        self.__logger.info("Starting DiscordClientWrapper...")
        self.run(self.__discord_token)

    async def on_ready(self):
        self.__logger.info(f"{self.user} has connected to Discord!")
        self.__discord_tasks_manager.start(self)

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
