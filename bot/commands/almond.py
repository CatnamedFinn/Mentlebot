import discord
from discord.ext import commands


@commands.command()
async def almond(ctx):
    await ctx.send("I like almonds.")


def setup(bot):
    # Every extension should have this function
    bot.add_command(almond)
