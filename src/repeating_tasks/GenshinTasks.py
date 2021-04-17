# Built-in imports
import asyncio

# Project imports
from src.data import Color, Config, Emoji
from src.utils.CommandHandler import CommandHandler
from src.utils import TimeUtil

# External imports
import discord
import schedule

# Async IO
LOOP = asyncio.get_event_loop()

# Genshin Channel ID
GENSHIN_CHANNEL_ID = 754050070349086720

# Genshin farming guides
DAYS_DOMAIN = {
    0: "[Mon] Talent books: Freedom/Prosperity; Weapon Mats: Decarabian/Guyun",
    1: "[Tue] Talent books: Diligence/Resistance; Weapon Mats: Mist Veiled Elixir/Boreal Wolf",
    2: "[Wed] Talent books: Ballad/Gold; Weapon Mats: Aerosiderite/Dandelion Gladiator",
    3: "[Thu] Talent books: Freedom/Prosperity; Weapon Mats: Decarabian/Guyun",
    4: "[Fri] Talent books: Diligence/Resistance; Weapon Mats: Mist Veiled Elixir/Boreal Wolf",
    5: "[Sat] Talent books: Ballad/Gold; Weapon Mats: Aerosiderite/Dandelion Gladiator",
    6: "[Sun] Talent books: ALL; Weapon Mats: ALL",
}


def change_description(bot):
    channel = bot.get_channel(GENSHIN_CHANNEL_ID)
    assert type(channel) is discord.TextChannel, "Invalid channel found!"

    async def edit():
        await channel.edit(topic=DAYS_DOMAIN[TimeUtil.get_now_weekday()])

    LOOP.create_task(edit())


###############################################################

def register_all(bot):
    """ Register all commands in this module """
    schedule.every().day.at("00:00").do(change_description, bot)
