import discord
from config import *

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_member_join(member: discord.Member):
    print(f"{member.display_name} joined")


@client.event
async def on_ready():
    print('Discord bot is ready')


client.run(token)
