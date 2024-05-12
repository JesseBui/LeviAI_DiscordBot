import discord
from discord.ext import commands
import yt_dlp
import asyncio

voice_clients = {}
queues = {}
yt_dl_options = {"format": "bestaudio/best"}
ytdl = yt_dlp.YoutubeDL(yt_dl_options)

ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                  'options': '-vn -filter:a "volume=0.25"'}


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('music is online')

    @commands.command()
    async def skip(self, ctx):
        if queues[ctx.guild.id] != []:
            # Fetch the first song in the queue
            link = queues[ctx.guild.id].pop(0)
            await self.play(ctx, link)

    @commands.command()
    async def play(self, ctx, link):
        try:
            if ctx.author.voice is None:
                return await ctx.send("join a channel lol")

            voice_client = await ctx.author.voice.channel.connect()
            voice_clients[ctx.guild.id] = voice_client
        except Exception as e:
            print(e)
        try:
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(link, download=False))

            song = data['url']
            player = discord.FFmpegOpusAudio(song, **ffmpeg_options)

            voice_clients[ctx.guild.id].play(player,
                                             after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(ctx),
                                                                                              self.bot.loop))
        except Exception as e:
            print(e)

    @commands.command()
    async def clear_queue(self, ctx):
        if ctx.guild.id in queues:
            queues[ctx.guild.id].clear()
            await ctx.send("Queue cleared!")
        else:
            await ctx.send("There is no queue to clear!")

    @commands.command()
    async def stop(self, ctx):
        try:
            voice_clients[ctx.guild.id].pause()
        except Exception as e:
            print(e)

    @commands.command()
    async def start(self, ctx):
        try:
            voice_clients[ctx.guild.id].resume()
        except Exception as e:
            print(e)

    @commands.command()
    async def leave(self, ctx):
        try:
            voice_clients[ctx.guild.id].stop()
            await voice_clients[ctx.guild.id].disconnect()
            del voice_clients[ctx.guild.id]
        except Exception as e:
            print(e)

    @commands.command()
    async def queue(self, ctx, url):
        if ctx.guild.id not in queues:
            queues[ctx.guild.id] = []
        queues[ctx.guild.id].append(url)
        await ctx.send("Added to queue!")


async def setup(bot):
    await bot.add_cog(Music(bot))
