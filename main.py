import discord
from config import *

client = discord.Client()


@client.event
async def on_ready():
    print('Discord bot is ready')

client.run(token)
