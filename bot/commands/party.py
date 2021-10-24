import discord
import re

from discord.ext import commands


games = {
    'lol': {
        'max_players': 5,
        'lobbies': [],
    },
    'genshin': {
        'max_players': 4,
        'lobbies': [],
    },
}


@commands.command(name='game')
async def party(ctx, action='', game=''):
    await ctx.send(
        "You need to specify what you want to do. "
        "Either `create` `join` `leave` or `disband`")


def setup(bot):
    # Every extension should have this function
    bot.add_command(party)
