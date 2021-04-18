# Built-in imports
import os

# Project imports
from src.Bot import BotClient
from src.commands import GuideCommands, UtilityCommands, TaterCommands
# from src.repeating_tasks import GenshinTasks
# from src.utils.ChatHandler import ChatHandler

# External imports
import discord

# Get Discord token from the environment
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create intent
intent = discord.Intents.default()
intent.members = True

# Create and start the client
bot = BotClient(intents=intent)

# Register commands
# NlpCommands.register_all(bot)
UtilityCommands.register_all(bot)
GuideCommands.register_all(bot)
TaterCommands.register_all(bot)

# Register NLP chat handler
# bot.register_chat_handler(ChatHandler(bot))

# Register repeating tasks
# GenshinTasks.register_all(bot)

bot.run(BOT_TOKEN)
