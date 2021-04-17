# Project imports
from src.data import Color, Config, Emoji
from src.utils import TimeUtil

# External imports
import discord


async def move_message(bot, message):
    """
    Move the current message to MOVE_TO channel (in config)

    Args:
        bot (BotClient): bot to perform action on
        message (discord.Message): message to move
    """
    # Generate message embedded
    embedded = generate_embedded(message.author, message.content, message.attachments)
    # Delete message
    await message.delete()
    # Send confirm message
    await message.channel.send(content=f"`{TimeUtil.formatted_now(include_date=True)}` >> Your report has been registered {Emoji.CHECK}")
    # Fetch MOVE_TO channel
    channel = await bot.fetch_channel(Config.MOVE_TO_CHANNEL)
    # Send message to MOVE_TO channel
    sent_message = await channel.send(embed=embedded)

    # Scan for attachments
    if not message.attachments:
        return

    # If there is attachments, send attachment messages
    for attachment in message.attachments:
        file = await attachment.to_file()
        await sent_message.reply(content=f"Attached file `{attachment.filename}`:", file=file)


def generate_embedded(author, raw_message, attachments):
    embedded = discord.Embed(
        title=f"Message from {author.display_name}#{author.discriminator}",
        description=f"Timestamp: {TimeUtil.formatted_now(include_date=True)}",
        color=Color.COLOR_HELP
    )
    if not raw_message:
        raw_message = "*no text message*"
    embedded.add_field(name="**Message from user:**", value=f"> {raw_message}", inline=False)
    if attachments:
        # Add attachments field
        embedded.add_field(name="**Message attachments:**", value=f"> {Config.SEP.join(att.filename for att in attachments)}", inline=False)
    return embedded
