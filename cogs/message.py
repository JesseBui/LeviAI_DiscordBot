import discord
from discord.ext import commands

class message(commands.Cog):
    def  __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("message is ready")
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content =="ai da ban do vay levi":
            await message.channel.send("""Rainbow Warriors: 
1. Nguyễn Kỳ Vương / Raze
2. Nguyễn Hoàng Nghĩa / HinieeeC
3. Nguyễn Trung Hiếu / Hyo
4. Nguyễn Anh Kiệt / Yuki
5. Nguyễn Phan Đình Khôi / Spot
6. Nguyễn Văn Hậu / Artifact
7. Vũ Quốc Hưng / K1ller
8. Nguyễn Trọng Trí / 2T
GAM Esports:
1. Đỗ Đình Sang / Blazes
2. Lê Viết Huy / Pyshiro
Team Flash:
1. Lê Minh Dũng / Dzung
2. Đinh Bùi Quốc Cường / Marcus
3. Lê Ngọc Toàn / Draktharr
4. Nguyễn Hoàng Khánh / Jane
5. Lương Thành Tài / Puddin
Team Secret: 
1. Hoàng Công Nghĩa / Eddie
2. Quách Khánh Hoàng / Qiang
Vikings Esports:
1. Lương Hải Long / Gury
2. Nguyễn Vũ Khang Nguyên / Bunn
3. Võ Văn Phi / Kairi
4. Ngô Đức Khánh / Kratos
Cerberus Esports:
1. Nguyễn Đăng Khoa / Pun
2. Trần Bảo Quang / Ikigai
3. Nguyễn Hoàng Phú / Richard I
4. Nguyễn Huy Hùng / Slowz
MGN Blue Esports:
1. Nguyễn Minh Hào / Sorn
2. Bùi Văn Minh Hải / Froggy
3. Võ Hoàng Lê Khang / Ryuk
4. Đào Văn Tuấn / Rigel
5. Tiêu Quốc Lương / Zodiac
Team Whales:
1. Trần Văn Chính / BeanJ
2. Lê Ngọc Vinh / Gloryy""")
        if message.content =="Quan":
            await message.channel.send(file= discord.File('Dam.jpg'))


async def setup(client):
    await client.add_cog(message(client))