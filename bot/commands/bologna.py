import discord
from discord.ext import commands


stored = 'bologna'


@commands.command()
async def bologna(ctx, arg, data):
    global stored
    if arg == 'read':
        await ctx.send(f"Stored data: {stored}")
    elif arg == 'write':
        if data == None:
            await ctx.send("What do you want to store?")
        else:
            stored = data
    else:
        await ctx.send("Do you want to `read` or `write`?")


def setup(bot):
    # Every extension should have this function
    bot.add_command(bologna)
