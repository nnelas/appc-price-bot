import logging

from bot.bot_provider import bot_provider

logging.basicConfig(level=logging.INFO)
discord_client = bot_provider.provide_discord_client_wrapper()
discord_client.start_client()
