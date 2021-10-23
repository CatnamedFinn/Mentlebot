import discord
from discord.ext import commands
import os

token = os.environ.get('DISCORD_TOKEN')
client = discord.Client()

bot = commands.Bot(command_prefix="!", case_insensitive=True)


async def bing(message):
    await message.channel.send('Bong.')


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content
    if content.startswith("!ver"):
        await message.channel.send("ver0")
    elif content.startswith("!bing"):
        bing(message)
    await bot.process_commands(message)


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("Pong.")

client.run(token)
