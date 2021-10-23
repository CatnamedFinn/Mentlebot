import discord
from discord.ext import commands
import os

token = os.environ.get('DISCORD_TOKEN')
client = discord.Client()

bot = commands.Bot(command_prefix="!", case_insensitive=True)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content
    if content.startswith("!ver"):
        await message.channel.send("ver1")
    await bot.process_commands(message)


@bot.command()
async def ping(ctx, message):
    await ctx.send(message)

client.run(token)
