import discord
from discord.ext import commands
import os


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
async def ping(ctx, message):
    await ctx.send(message)
    await message.channel.send('I dunno man')

bot.run(token)
