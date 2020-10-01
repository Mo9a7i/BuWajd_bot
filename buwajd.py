import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix='$')


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
        await get_categories(guild)
        await get_channels(guild)
        # await get_users(guild)


async def get_categories(guild):
    for category in guild.categories:
        print(f'{category.name}(id: {category.id}')

async def get_channels(guild):
    for channel in guild.channels:
        print(f'{channel.name}(id: {channel.id}')
        if channel.id == 459699169062420481:
            await channel.send('Hello from Channel')

async def get_users(guild):
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command(pass_context=True)
async def addstreamer(ctx, twitch_name, discord_name: discord.Member):
    #make sure its a valid admin
    if(ctx.message.author.name == "BuFai7an"):
        guild = ctx.message.guild
        await ctx.send("Hello Mohannad, you wanted to create a room for " + twitch_name)

        #discord_user = discord.utils.get(guild.members, name=discord_name)
        if discord_name != None:

            # Create the Channel
            streamers_category = discord.utils.get(guild.categories, id=711828559588491348)
            channel = await guild.create_text_channel(twitch_name,category=streamers_category)
            print(channel.id)
            
            # Add the member to the streamers role
            streamers_role = discord.utils.get(guild.roles, id=747879586020327476)
            print(streamers_role.id)
            for roly in guild.roles:
                print(f'{roly.name}(id: {roly.id}')
                
            # discord_user = discord.utils.get(guild.members, name=discord_name)
            await discord_name.add_roles(streamers_role)


# bot.run(TOKEN)

client.run(TOKEN)



# run the whole
