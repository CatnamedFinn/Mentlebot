import discord
from discord.ext import commands

bot = None


@commands.command()
async def almond(ctx):
    if bot != None:
        message_channel = bot.get_channel(901007512311070731)
        await ctx.send(message_channel)
    else:
        await ctx.send("I like almond-scented channels.")


def setup(parent_bot):
    global bot
    # Every extension should have this function
    parent_bot.add_command(almond)
    bot = parent_bot
