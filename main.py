import discord
from discord.ext import commands
import requests
import json
from discord import Webhook
import aiohttp
import random 

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix = '*', intents=intents)

VCS = ["VKE","GAM"]

@client.event
async def on_ready():
    print('Bot is ready.')


#Levi snitch
@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content =="ai da ban do vay levi":
        await message.channel.send("Rainbow Warriors:\n1. Nguyễn Kỳ Vương / Raze\n2. Nguyễn Hoàng Nghĩa / HinieeeC\n3. Nguyễn Trung Hiếu / Hyo\n4. Nguyễn Anh Kiệt / Yuki\n5. Nguyễn Phan Đình Khôi / Spot\n6. Nguyễn Văn Hậu / Artifact\n7. Vũ Quốc Hưng / K1ller\n8. Nguyễn Trọng Trí / 2T\nGAM Esports:\n1. Đỗ Đình Sang / Blazes\n2. Lê Viết Huy / Pyshiro\nTeam Flash:\n1. Lê Minh Dũng / Dzung\n2. Đinh Bùi Quốc Cường / Marcus\n3. Lê Ngọc Toàn / Draktharr\n4. Nguyễn Hoàng Khánh / Jane\n5. Lương Thành Tài / Puddin\nTeam Secret:\n1. Hoàng Công Nghĩa / Eddie\n2. Quách Khánh Hoàng / Qiang\nVikings Esports:\n1. Lương Hải Long / Gury\n2. Nguyễn Vũ Khang Nguyên / Bunn\n3. Võ Văn Phi / Kairi\n4. Ngô Đức Khánh / Kratos\nCerberus Esports:\n1. Nguyễn Đăng Khoa / Pun\n2. Trần Bảo Quang / Ikigai\n3. Nguyễn Hoàng Phú / Richard I\n4. Nguyễn Huy Hùng / Slowz\nMGN Blue Esports:\n1. Nguyễn Minh Hào / Sorn\n2. Bùi Văn Minh Hải / Froggy\n3. Võ Hoàng Lê Khang / Ryuk\n4. Đào Văn Tuấn / Rigel\n5. Tiêu Quốc Lương / Zodiac\nTeam Whales:\n1. Trần Văn Chính / BeanJ\n2. Lê Ngọc Vinh / Gloryy")
    if message.content =="Quan":
        await message.channel.send(file= discord.File('Dam.jpg'))# Levi Will send an Image
    if message.content =="ai vo dich vcs":
        await message.channel.send(random.choice(VCS)) #Levi Will print random stuff from the array above

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("dmm")
    


@client.command()
async def hello(ctx):
    await ctx.send('chao moi nguoi, tui ghet ban do')

@client.command()
async def opgg_khang(ctx):
    await ctx.send('https://www.op.gg/summoners/na/우리%20팀에%20소아성애자%205명-Bui')

@client.command()
async def opgg_kiet(ctx):
    await ctx.send('https://www.op.gg/summoners/na/우리팀에소아성애자5명-Lam')

@client.command()
async def opgg_quan(ctx):
    await ctx.send('https://www.op.gg/summoners/na/e1zm-Mzie')

@client.command()
async def opgg_chit(ctx):
    await ctx.send('https://www.op.gg/summoners/na/네엄마는나쁜년이야-666')

@client.command()
async def opgg_shiloh(ctx):
    await ctx.send('https://www.op.gg/summoners/na/엄마%20엿%20먹어-1001')

@client.command()
async def opgg_tean(ctx):
    await ctx.send('https://www.op.gg/summoners/na/내가%20널%20아주%20세게%20때려줄게-1234')




#Levi will tell you joke
@client.command()
async def joke(ctx):
    url = "https://daddyjokes.p.rapidapi.com/random"
    headers = {
	"X-RapidAPI-Key": "tokenkey",
	"X-RapidAPI-Host": "daddyjokes.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    await ctx.send(json.loads(response.text)['joke'])
    print('Levi has printed a joke')


#Levi will tell you weather
@client.command()
async def weather(ctx ,*, city):
    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": 'tokenkey',
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

client.run('token')