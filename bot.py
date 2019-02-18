import discord
import asyncio
import time
from discord.ext import commands
import random
import config

#Token file has the token saved.
token = config.bbtoken
descript = config.des #To get the bot description
client = commands.Bot(command_prefix= config.pref, description= descript)


@client.event  # event decorator/wrapper.P
async def on_ready():  # method expected by bot. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.
    await client.change_presence(activity=discord.Game(name='Toram Online'))

@client.event
async def on_message(message):
    #print(f"{message.guild}: {message.author}: {message.content}") #to log the chats.
    if message.content == '<@501968572998746143>':
        await message.channel.send(f"The prefix of the bot is {config.pref}") #Ping the bot to know it's prefix.
    await client.process_commands(message)

@client.event
async def on_member_join(member):
    if member.guild.id == 503745835448795166:
        channel = member.guild.get_channel(503745835448795168)
        await channel.send(f"Hey {member.mention}, welcome to the land of the **{member.guild}** :tada::cyclone::star2: !")
        

@client.event
async def on_member_remove(member):
    if member.guild.id == 503745835448795166:
        channel = member.guild.get_channel(503745835448795168)
        await channel.send(f"**{member.name}{member.discriminator}** quit their Schaduw journey and went to the Light :ghost:")

@client.command()
async def logout(ctx):
    '''Used to Logout the bot'''
    if ctx.author.id == 362645647545073685:
        await ctx.send('Logging out...')
        await client.logout() #command to logout the bot.
    else:
        await ctx.send("You don't have the required permissions.")

@client.command(aliases= ['hi', 'hey'])
async def hello(ctx):
    '''Say hello to the bot'''
    await ctx.send(f"Hello {ctx.author.name}")
    print(f"{ctx.author.guild.channels}")

@client.command(aliases= ['random', 'dice', 'rng'])
async def roll(ctx, arg1: int = 1, arg2: int = 6):
    '''To generate random numbers.'''
    if arg2 == 6 and arg1 != 1:
        await ctx.send(f"You have rolled {random.randint(1, arg1)}")
    else:
        await ctx.send(f"You have rolled {random.randint(arg1, arg2)}")

@client.command()
async def ping(ctx):
    '''To ping the user of the command'''
    await ctx.send(f"{ctx.message.author.mention} Pong!")

@client.command()
async def insult(ctx, member: discord.Member = None):
    '''Says something mean about you or the person you mentioned.'''
    if member == None:
        await ctx.send(f"{ctx.message.author.mention}  {random.choice(config.insults)}")  # Mention the user and say the insult
    else:
        await ctx.send(f"{member.mention} {random.choice(config.insults)}")

@client.command(aliases=['delete', 'clear', 'purge'])
@commands.has_permissions(manage_messages=True)
async def prune(ctx, number: int = 10):
    '''Bulk-deletes messages from the channel.'''
    msgs = []
    async for msg in ctx.channel.history(limit = number + 1): #used to iterate over the messages.
        msgs.append(msg)
    await ctx.channel.delete_messages(msgs) #used to delete messages from the given list.
    print(f"Pruned {number} messages.")
    await ctx.send(f"Pruned {number} messages.")

client.run(token)
