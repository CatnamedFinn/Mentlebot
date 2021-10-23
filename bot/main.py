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
    await ctx.send(message)
    await message.channel.send('I dunno man')


bot.run(token)
