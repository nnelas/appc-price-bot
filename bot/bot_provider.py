import os
from typing import Optional

from appc.appc_provider import appc_provider
from bot.discord_client_wrapper import DiscordClientWrapper
from bot.discord_tasks_manager import DiscordTasksManager


class BotProvider:
    def __init__(self):
        self.__appc_price_repository = appc_provider.provide_appc_price_repository()
        self.__token = self.__get_discord_token()
        self.__discord_tasks_manager = DiscordTasksManager(
            817374892378947651, self.__appc_price_repository
        )

    def provide_discord_client_wrapper(self) -> DiscordClientWrapper:
        return DiscordClientWrapper(
            self.__appc_price_repository,
            self.__token,
            self.__discord_tasks_manager,
        )

    def __get_discord_token(self) -> Optional[str]:
        if os.getenv("DISCORD_BOT_TOKEN") is None:
            raise Exception(
                "Unable to get DISCORD_BOT_TOKEN. Please make sure that you "
                "have added it into your environment variables."
            )
        return os.getenv("DISCORD_BOT_TOKEN")


bot_provider = BotProvider()
