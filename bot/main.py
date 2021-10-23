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
    if message.content.startswith("!hello"):
        await message.channel.send("test")


@bot.command()
async def ping(ctx):
    await ctx.channel.send("Pong.")

client.run(token)
