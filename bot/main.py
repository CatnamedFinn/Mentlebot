import discord
from discord.ext import commands
import os

token = os.environ.get('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.command()
async def ping(ctx, message):
    await ctx.channel.send(message)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    content = message.content
    if content.startswith("!ver"):
        await message.channel.send("ver3")
    elif content.startswith("!hi"):
        await message.channel.send("Hello.")
    else:
        await bot.process_commands(message)


bot.run(token)
