import discord
from discord.ext import commands
import yt_dlp
import os
from youtube_search import YoutubeSearch
import json
import asyncio

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loop = False  # check if loop is active
        self.current_song = None  # check what song is playing
        self.queues = {}  # dictionary to store queues for each guild

        # Delete 'song.mp3' if it exists so it will not interfere with the bot
        if os.path.exists("song.mp3"):
            os.remove("song.mp3")

    async def check_queues(self, id):
        if self.queues[id] != []:
            voice = discord.utils.get(self.bot.voice_clients, guild=id)
            if self.loop:
                voice.play(discord.FFmpegPCMAudio(self.current_song))
            else:
                source = self.queues[id].pop(0)
                voice.play(source)
                self.current_song = source

    @commands.command()
    async def play(self, ctx, *, url=None):
        if url is None:
            if self.loop:
                url = self.current_song
            else:
                return

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice is None:
            channel = ctx.author.voice.channel
            voice = await channel.connect()

        if voice.is_playing() or voice.is_paused():
            if ctx.guild.id in self.queues:
                self.queues[ctx.guild.id].append(url)
            else:
                self.queues[ctx.guild.id] = [url]
            await ctx.send("Song added to queue.")
        else:
            if not ctx.author.voice:
                await ctx.send("You must be in a voice channel to run this command")
                return

            voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            if voice is None:
                channel = ctx.author.voice.channel
                voice = await channel.connect()

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                }],
            }

            if "http" not in url:
                yt = YoutubeSearch(url, max_results=1).to_json()
                print(yt)
                yt_id = str(json.loads(yt)['videos'][0]['id'])
                yt_channel = str(json.loads(yt)['videos'][0]['channel']).strip().replace(" ", "")
                url = 'https://www.youtube.com/watch?v=' + yt_id + "&ab_channel=" + yt_channel

            self.current_song = url
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                info = ydl.extract_info(url, download=False)
                title = info.get('title', None)

            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
                    break

            voice.play(discord.FFmpegPCMAudio("song.mp3"),
                       after=lambda e: self.bot.loop.create_task(self.play(ctx, url=self.current_song)))

            embed = discord.Embed(
                title="Hiện đang chơi ",
                description=f"[{title}]({url})",
                color=discord.Color.yellow()
            )
            await ctx.send(embed=embed)
            await asyncio.sleep(1)  # Wait for the song to start playing

    @commands.command()
    async def stop(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice is not None:
            voice.stop()
        if os.path.exists("song.mp3"):
            os.remove("song.mp3")

    @commands.command()
    async def loop(self, ctx):
        self.loop = not self.loop
        await ctx.send(f"Vòng lặp đang được {'Bật' if self.loop else 'Tắt'}.")

async def setup(client):
    await client.add_cog(Music(client))
