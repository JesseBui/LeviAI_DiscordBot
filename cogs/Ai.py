from discord.ext import commands
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv() 

client = OpenAI(
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
                                Auto-switch language based on the input. Stay cocky, stay cracked."""
            }
        ]

    @commands.Cog.listener()
    async def on_ready(self):
        print("chatgpt is ready")

    """
    split content to comply with 2000 word limit by discord
    i = start : i+limit = end 
    """
    def split_text(self,text,limit = 2000):
        return [text[i: i+limit] for i in range(0, len(text), limit)]
    
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
            return
        
        try:
            print("testing sending request to openai")
            response = client.chat.completions.create(
                model="gpt-5.1",
                messages= self.memory,
                temperature=0.5,
                top_p=1, #max unpredictable
                frequency_penalty=0,
            )

            assisstant_reply = response.choices[0].message.content



            self.memory.append({"role": "assistant", "content": assisstant_reply})
            print(f"assisstant reply {assisstant_reply}")
            print(message.content+ " was send to Levi"+ " and his response was "+assisstant_reply)

            if len(assisstant_reply) > 1900: 
                words = self.split_text(assisstant_reply)
                for word in words:
                    await message.channel.send(word)
            else:
                await message.channel.send(assisstant_reply)
        
        except Exception as e:
            # This will tell you exactly why it's failing in your console
            print(f"ERROR: {e}") 
            await message.channel.send(f"Levi crashed: {e}")

    @commands.command()
    async def clear(self,ctx):
        self.memory = [self.memory[0]]
        await ctx.send("memory reset beep boop")
        print(self.memory)
            
async def setup(client):
    await client.add_cog(Ai(client))
