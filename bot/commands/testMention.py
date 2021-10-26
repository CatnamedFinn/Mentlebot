import discord
from discord.ext import commands

@commands.command()
async def mention(ctx):
    mention = ctx.author.mention
    await ctx.send(f"Hey {mention}!")

def setup(bot):
    # Every extension should have this function
    bot.add_command(mention)