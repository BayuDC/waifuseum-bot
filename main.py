import discord
from config import *

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)


@client.event
async def on_guild_channel_create(channel):
    if (type(channel) is not discord.TextChannel):
        return
    if (channel.category_id != ids['parent']):
        return

    print("Channel created")


@client.event
async def on_member_join(member: discord.Member):
    role_id = ids['member']
    role = member.guild.get_role(role_id)
    await member.add_roles(role)


@client.event
async def on_ready():
    print('Discord bot is ready')


client.run(token)
