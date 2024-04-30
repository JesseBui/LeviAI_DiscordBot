import discord
from discord.ext import commands
import aiohttp
from dotenv import load_dotenv
import os

load_dotenv()


class Weather(commands.Cog):
    def  __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("weather is ready") 
    
    #Levi will tell you the weather
    @commands.command()
    async def weather(self,ctx ,*, city):
        url = "https://api.weatherapi.com/v1/current.json"
        params = {
        "key": os.getenv("weatherkey"),
        "q": city
    }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as res:
                data = await res.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        embed = discord.Embed(title="Thời tiết của "+location, description="Trời của "+country +" Đang "+condition)
        embed.set_author(name ="levi" , url="https://twitter.com/lolLevi97")
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/lolesports_gamepedia_en/images/e/e9/GAM_Levi_2024_Split_1.png/revision/latest?cb=20240306180739")
        embed.add_field(name = "Nhiệt độ: ", value= str(temp) +"°c")
        
        await ctx.send(embed=embed)
        print("Levi has print the weather")
        

async def setup(client):
    await client.add_cog(Weather(client))