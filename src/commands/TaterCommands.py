# Project imports
from src.utils import TimeUtil, MoveMessageUtil
from src.utils.CommandHandler import CommandHandler
from src.data import Color, Config, Emoji

# External imports
import discord


# TODO: isinstance(channel, discord.DMChannel)


class DmReportCommandHandler(CommandHandler):
    def __init__(self, bot):
        super().__init__(bot, "report", ["vent"], "[DM Only] Report something to the moderators in AaH Discord", f"{Config.BOT_PREFIX}report [message...]", f"{Config.BOT_PREFIX}report I ate too many strawberries!")

    async def on_command(self, author, command, args, message, channel, guild):
        # DM-only command
        if not isinstance(channel, discord.DMChannel):
            await self.bot.reply(message, "This command is usable in direct message (DM) channels only!")
            return

        # Help in general
        if len(args) == 0:
            await self.bot.reply(message, content="Invalid report arguments!", embedded=self.get_help_embedded())
            return

        # Generate message embedded
        embedded = MoveMessageUtil.generate_embedded(message.author, message.content, message.attachments, is_dm=True)

        # Fetch MOVE_TO channel and send message
        channel = await self.bot.fetch_channel(Config.MOVE_TO_CHANNEL)
        sent_message = await channel.send(embed=embedded)

        # Send confirm message
        await self.bot.reply(message, content=f"`{TimeUtil.formatted_now(include_date=True)}` >> Your report has been registered {Emoji.CHECK}")

        # Send attachments if there are attachments
        if message.attachments:
            for attachment in message.attachments:
                file = await attachment.to_file()
                await sent_message.reply(content=f"Attached file `{attachment.filename}`:", file=file)


###############################################################

def register_all(bot):
    """ Register all commands in this module """
    bot.register_command_handler(DmReportCommandHandler(bot))
