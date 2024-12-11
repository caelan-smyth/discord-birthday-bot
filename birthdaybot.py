import datetime
import os
from typing import Generator
from discord import Intents, Client, Message
from discord.member import Member
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

class Client(Client):
    async def on_ready(self):
        print(f"{client.user} has connected to Discord!")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")

intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)

client.run(TOKEN)