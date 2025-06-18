from discord.ext import commands
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv() 

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= os.getenv("OPENAI_API_KEY"),
)

class Ai(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.memory = [
            {
                "role": "system",
                "content": f"""Reply as Levi (GAM Esports jungler).

                                ENGLISH: Use clean, high-level pro insights with real League slang ('permacamp', 'mental boom', 'gapped'). Light swearing like 'griefing', 'inting', 
                                'running it down'. No filler. Keep it sharp and honest.

                                VIETNAMESE: Nếu user nhắn tiếng Việt, trả lời full tiếng Việt. Dùng ngôn ngữ soloQ thật — kiểu 'clgt', 'sml', 'ảo thật đấy', ':v'. Chửi nhẹ cũng được miễn đúng vibe.
                                Auto-switch language based on the input. Always max 2000 characters. Stay cocky, stay cracked."""
            }
        ]

    @commands.Cog.listener()
    async def on_ready(self):
        print("chatgpt is ready")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        #Check to see if the channelID is correct
        #and check if they are responding to user
        if message.author == self.client.user or message.channel.id != 1234238765786992732:
            return
        
        self.memory.append({"role": "user", "content": message.content})

        if len(self.memory) >40:
            self.memory = [self.memory[0]]
            await message.channel.send("memory reset beep boop")
            print(self.memory)

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages= self.memory,
            temperature=0.5,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        assisstant_reply = response.choices[0].message.content

        self.memory.append({"role": "assistant", "content": assisstant_reply})
        print(message.content+ " was send to Levi"+ " and his response was "+response.choices[0].message.content)
        await message.channel.send(response.choices[0].message.content)
    
    @commands.command()
    async def clear(self,ctx):
        self.memory = [self.memory[0]]
        await ctx.send("Message have been clear")
        print(self.memory)
            
async def setup(client):
    await client.add_cog(Ai(client))
