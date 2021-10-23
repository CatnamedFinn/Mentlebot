import discord
import os
import re

from discord.ext import commands
from enum import Enum

token = os.environ.get('DISCORD_TOKEN')
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


class TicTacToeStateType(Enum):
    NOT_PLAYING = 1
    LOBBYING = 2
    PLAYING = 3


ticTacToeState = TicTacToeStateType.INACTIVE
ticTacToePlayers = []
ticTacToeTurn = 0
ticTacToeBoard = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    content = message.content

    if content.startswith("!ver"):
        await message.channel.send("ver8")
    elif content.startswith("!hi"):
        await message.channel.send("Hello.")
    await bot.process_commands(message)


@bot.command()
async def sussify(ctx):
    message = ctx.message

    if message.reference is None:
        await ctx.send("You need to reply to a message in order to sussify it.")
        return

    replyId = message.reference.message_id
    reply = await ctx.channel.fetch_message(replyId)
    content = reply.content

    await ctx.send(f"Your message is in reply to this one: '{content}'")

    sussified = re.sub("[^s.*u.*s]", "█", content)
    await ctx.send(sussified)


@bot.command(name='3d3t')
async def _3d3t(ctx, arg1, arg2):
    global ticTacToeState, ticTacToePlayers, ticTacToeTurn, ticTacToeBoard

    if ticTacToeState == TicTacToeStateType.NOT_PLAYING:
        # start lobbying
        ticTacToeState = TicTacToeStateType.LOBBYING
        ticTacToePlayers.insert(ctx.author)
        return

    if ticTacToeState == TicTacToeStateType.LOBBYING:
        # keep lobbying
        playerCount = len(ticTacToePlayers)
        ticTacToePlayers.insert(ctx.author)
        await ctx.send(f"{ctx.author.display_name} has joined as Player {playerCount}!")

        if playerCount == 2:
            await ctx.send("Max players reached. Starting game now!")
            ticTacToeState = TicTacToeStateType.PLAYING
        return

    if ticTacToeState == TicTacToeStateType.PLAYING:
        # end the game
        if arg1 == 'stop':
            await ctx.send("Ending game now...")
            ticTacToeState = TicTacToeStateType.NOT_PLAYING
            return
        # not a player
        if ctx.author not in ticTacToePlayers:
            await ctx.send("You're not even playing right now.")
            return
        # wrong player
        if ctx.author != ticTacToePlayers[ticTacToeTurn]:
            await ctx.send("Now's not your turn.")
            return
        await ctx.send(f"Player {ticTacToeTurn} has made their move.")
        ticTacToeTurn = (ticTacToeTurn + 1) % 2
        return

    '''
    board = ''
    for row in ticTacToeBoard:
        board += f"| {row[0]} | {row[1]} | {row[2]} |\n"

    await ctx.send(
        "```"
        "Player 1 has made their move!"
        f"{board}"
        "```"
        "Player 2, specify your next coordinates."
    )
    '''

bot.run(token)
