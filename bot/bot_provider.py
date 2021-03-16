import os
from typing import Optional

from appc.appc_provider import appc_provider
from bot.discord_client_wrapper import DiscordClientWrapper


class BotProvider:
    def __init__(self):
        self.__appc_price_repository = appc_provider.provide_appc_price_repository()
        self.__token = self.__get_discord_token()

    def provide_discord_client_wrapper(self) -> DiscordClientWrapper:
        return DiscordClientWrapper(
            self.__appc_price_repository, self.__token, 817374892378947651
        )

    def __get_discord_token(self) -> Optional[str]:
        if os.getenv("DISCORD_BOT_TOKEN") is None:
            raise Exception(
                "Unable to get DISCORD_BOT_TOKEN. Please make sure that you "
                "have added it into your environment variables."
            )
        return os.getenv("DISCORD_BOT_TOKEN")


bot_provider = BotProvider()
