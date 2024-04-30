import discord
from discord.ext import  commands

class Opgg(commands.Cog):
    def  __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("opgg is ready")    
    
    @commands.command()
    async def hello(self,ctx):
        await ctx.send('chao moi nguoi, tui ghet ban do')

    @commands.command()
    async def opgg_khang(self,ctx):
        await ctx.send('https://www.op.gg/summoners/na/우리%20팀에%20소아성애자%205명-Bui')

    @commands.command()
    async def opgg_kiet(self,ctx):
        await ctx.send('https://www.op.gg/summoners/na/우리팀에소아성애자5명-Lam')

    @commands.command()
    async def opgg_quan(self,ctx):
        await ctx.send('https://www.op.gg/summoners/na/e1zm-Mzie')

    @commands.command()
    async def opgg_chit(self,ctx):
        await ctx.send('https://www.op.gg/summoners/na/네엄마는나쁜년이야-666')

    @commands.command()
    async def opgg_shiloh(self,ctx):
        await ctx.send('https://www.op.gg/summoners/na/엄마%20엿%20먹어-1001')

    @commands.command()
    async def opgg_tean(self,ctx):
        await ctx.send('https://www.op.gg/summoners/na/내가%20널%20아주%20세게%20때려줄게-1234')




async def setup(client):
    await client.add_cog(Opgg(client))