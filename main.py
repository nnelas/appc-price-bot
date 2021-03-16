import logging

from bot.bot_provider import bot_provider

logging.basicConfig(level=logging.INFO)
bot_provider.provide_discord_client_wrapper()
