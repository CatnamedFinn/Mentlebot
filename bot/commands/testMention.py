import discord
from discord.ext import commands

@commands.command()
async def mention(ctx):
    mention = ctx.author.mention
    await ctx.send(f"Hey {mention}!")