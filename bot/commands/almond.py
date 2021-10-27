import discord
from discord.ext import commands


@commands.command()
async def almond(ctx):
    await ctx.send("I like almond-scented channels.")


def setup(parent_bot):
    # Every extension should have this function
    parent_bot.add_command(almond)
