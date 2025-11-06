from discord.ext import commands
import requests
from lxml import html


#TODO: use less hardcode methods. doesn't work rn.
class Monster2(commands.Cog):
    def init(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} is ready")
        
    @commands.command()
    async def mon(self,ctx,*,mon):
        base_url = "https://monsterhunterwiki.org/wiki/"
        firstLetter = mon.title()
        monster = firstLetter.replace(" ", "_")
        url = base_url + monster +"_(MHWilds)"
        print (url)
        page = requests.get(url)
        
        tree = html.fromstring(page.content)
        length = len(tree.xpath("//tr[th[contains(text(), 'Weakest To')]]/td/span/span/a"))
        for i in range(length):
            info = tree.xpath("//tr[th[contains(text(), 'Weakest To')]]/td/span/span/a")[i]
            weakness = info.get('title') 
            print (weakness)
            await ctx.channel.send("Monster weakness is: " + weakness)

async def setup(client):
    await client.add_cog(Monster2(client))