import discord
from discord.ext import commands

@commands.command()
async def mention(ctx):
    mention = ctx.author.display_name
    await ctx.send(f"Hey {mention.mention}!")

def setup(bot):
    # Every extension should have this function
    bot.add_command(mention)