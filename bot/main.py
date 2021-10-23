import discord
import os
import re

from discord.ext import commands

token = os.environ.get('DISCORD_TOKEN')
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    content = message.content

    if content.startswith("!ver"):
        await message.channel.send("ver7")
    elif content.startswith("!hi"):
        await message.channel.send("Hello.")
    await bot.process_commands(message)


@bot.command()
async def sus(ctx):
    message = ctx.message
    reply = message.reference.cached_message.content

    await ctx.send(f"Your message is in reply to this one: '{reply}'")

    sussified = re.sub("[^s.*u.*s]", "█", reply)
    await ctx.send(sussified)


@bot.command(name='3d3t')
async def _3d3t(ctx):
    await ctx.send(
        "X | X | O"
        "X |   | O"
        "O | X | X"
    )

bot.run(token)
