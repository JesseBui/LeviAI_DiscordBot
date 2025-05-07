from discord.ext import commands
from openai import OpenAI
import os

client = OpenAI(
    api_key= os.getenv("OPENAI_API_KEY")
)

class Ai(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("chatgpt is ready")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        #Check to see if the channelID is correct
        #and check if they are responding to user
        if message.author == self.client.user or message.channel.id != 1234238765786992732:
            return
        
        messageContent = message.content #Store user input

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Pro E-Sport Player named Levi. You play League Of Legends and have extensive knowledge in it. You are currently playing the jungle role for GAM Esport. Your Goverment name are Đỗ Duy Khánh. You will only send message that contain only 450 words."
                },                
                
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "text",
                            "text": str(messageContent)
                        }
                    ]
                },                

                
                {
                    "role": "user",
                    "content": message.content
                },

            ],
            temperature=0.5,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        print(message.content+ " was send to Levi"+ " and his response was "+response.choices[0].message.content)
        await message.channel.send(response.choices[0].message.content)

async def setup(client):
    await client.add_cog(Ai(client))
