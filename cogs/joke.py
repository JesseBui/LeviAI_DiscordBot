from discord.ext import commands
import json
import requests
from  dotenv import load_dotenv
import os

load_dotenv()

class Joke(commands.Cog):
    def  __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("joke is ready")
    
    #Levi will tell you joke
    @commands.command()
    async def joke(self,ctx):
        url = "https://daddyjokes.p.rapidapi.com/random"
        headers = {
	    "X-RapidAPI-Key": os.getenv("jokekey"),
	    "X-RapidAPI-Host": "daddyjokes.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        await ctx.send(json.loads(response.text)['joke'])
        print('Levi has printed a joke')

async def setup(client):
    await client.add_cog(Joke(client))