# Import Modules
import os
import discord
import aiohttp
import random
import asyncio
import datetime
from dotenv import load_dotenv
from discord import Client
from discord.ext import commands
from discord.ext.commands import CommandNotFound, has_permissions, MissingPermissions
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

# Bot Information
version = "2.0.1"
permissions = 8

# Load the .ENV File
load_dotenv("assets/secrets/TOKEN.env")

# Message in Terminal
print(f"Eric's Discord Bot Revision Version {version}")

# Set Bot Prefix
bot = commands.Bot(command_prefix="!", description="Eric's Discord Bot Revision Version {}".format(version))

# Send Message on Bot Ready
@bot.event
async def on_ready():
    DiscordComponents(bot, change_discord_methods=True)
    await bot.change_presence(activity=discord.Game(name="!help"))
    print("Bot has successfully logged in as: {}".format(bot.user))
    print("Bot ID: {}\n".format(bot.user.id))

# Change the Bot's Game
async def randomgame():
    await bot.wait_until_ready()
    status = -1
    while not bot.is_closed():
        if status == 2:
            status = 0
        else:
            status += 1
        statuses = ["!help",f"on {len(bot.guilds)} guilds!","Type !invite to Invite me to your Server!"]
        gamename = statuses[status]
        await bot.change_presence(activity=discord.Game(name=gamename))
        await asyncio.sleep(5)
bot.loop.create_task(randomgame())

# Invite Command
@bot.command(pass_context=True)
async def invite(ctx):
    await ctx.reply(type=InteractionType.ChannelMessageWithSource, content="Click the Button Below to Invite the Bot", components=[Button(style=ButtonStyle.URL, label="Invite", url="https://discord.com/api/oauth2/authorize?client_id=850765009440866384&permissions=8&scope=bot"), Button(style=ButtonStyle.blue, label="Get Link")])
    res = await bot.wait_for("button_click")
    await res.respond(type=InteractionType.ChannelMessageWithSource, content='Invite Link: https://discord.com/api/oauth2/authorize?client_id=850765009440866384&permissions=8&scope=bot')
# Retreive the Token
token = os.getenv("TOKEN")

# Run the Bot
bot.run(token)
