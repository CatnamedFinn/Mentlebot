import discord
from discord.ext import commands
import os

token = os.environ.get('DISCORD_TOKEN')
client = discord.Client()

bot = commands.Bot(command_prefix="!", case_insensitive=True)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@bot.command()
async def ping(ctx, message):
    await ctx.channel.send(message)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content
    if content.startswith("!ver"):
        await message.channel.send("ver3")
    elif content.startswith("!hi"):
        await message.channel.send("Hello.")
    else:
        await bot.process_commands(message)


client.run(token)
