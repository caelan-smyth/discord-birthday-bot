import datetime
import os
from discord import Intents, Client, Message
from dotenv import load_dotenv

intents = Intents(presences=True, messages=True, members=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = Client(intents=intents)

@client.event
async def on_ready():
    memberlist = []
    for guild in client.guilds:
        if guild.id == GUILD:
            break

    for member in guild.members:
        memberlist.append(member.name)
    
    print(
        f"User ID:{client.user.id} Name: {client.user.name} has connected to Discord!"
        f"{guild.name}(id: {guild.id})"
    )

    print(memberlist)

client.run(TOKEN)