# Project imports
from src.utils.CommandHandler import CommandHandler
from src.data import Color, Config, Emoji, Messages

# External imports
import discord


# Genshin Channel ID = 754050070349086720

# 16:40 every Tues
class GuideCommandHandler(CommandHandler):
    def __init__(self, bot):
        super().__init__(bot, "guide", ["guides"], "Show the general guide of AaH", "", "")

    async def on_command(self, author, command, args, message, channel, guild):
        await self.bot.reply(message, content=Messages.GUIDE_ALL)


###############################################################

def register_all(bot):
    """ Register all commands in this module """
    bot.register_command_handler(GuideCommandHandler(bot))
