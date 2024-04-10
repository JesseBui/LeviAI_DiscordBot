import discord
from discord.ext import commands
import os
import asyncio
import apikey 

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '*', intents=intents)

#Load the cogs to the main file
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

#Start the bot
async def main():
    async with client:
        await load()
        await client.start(apikey.tokenbot)

@client.event
async def on_ready():
    print('Levi is online')

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("dmm")


asyncio.run(main())