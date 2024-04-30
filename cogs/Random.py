from discord.ext import commands
import random

arr = ["yes", "no", "maybe"]


class Ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("8ball is ready")

    @commands.command()
    async def ball(self, ctx):
        answer = random.choice(arr)
        await ctx.send(answer)


class Number(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Number is ready")
    
    @commands.command()
    async def number(self, ctx):
        # check to see if the sender is responding in the same channel 
        # and to see if message can be converted into digit
        def check(msg):
            return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel
        
        await ctx.send("First number")
        msg = await self.client.wait_for("message", check = check)
        
        await ctx.send("Second number(must be larger than the first)")
        msg2 = await self.client.wait_for("message", check = check)
        
        x = int(msg.content)
        y = int(msg2.content)

        if x < y :
            value = random.randint(x , y)
            await ctx.send(value)
        else : 
            await ctx.send("???")
        

async def setup(client):
    await client.add_cog(Ball(client))
    await client.add_cog(Number(client))
