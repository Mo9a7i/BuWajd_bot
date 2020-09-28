import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


# TODO: Should announe a stream once twitch stream started from any of the streamers group.

#  ! Will print something once connected
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await get_guilds()

# if someone sends a message hello, it will reply hello
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# gets a list of all guilds the bot is connected to
async def get_guilds():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
        await get_channels(guild)
        await get_users(guild)

# gets a list of all channels in a guild
async def get_channels(guild):
    for channel in guild.channels:
        print(f'{channel.name}(id: {channel.id}')
        if channel.id == 459699169062420481:
            await channel.send('Hello from Channel')

# gets all users of a guild
async def get_users(guild):
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


# run the whole
client.run(TOKEN)