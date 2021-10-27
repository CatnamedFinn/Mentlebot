import discord
from discord.ext import commands

bot = None


@commands.command()
async def almond(ctx):
    if bot != None:
        message_channel = bot.get_channel(901007512311070731)
        await ctx.send(message_channel)
    await ctx.send("I like almonds.")


def setup(parent_bot):
    # Every extension should have this function
    parent_bot.add_command(almond)
    bot = parent_bot
