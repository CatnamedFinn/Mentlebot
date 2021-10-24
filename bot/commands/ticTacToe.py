import discord

from discord.ext import commands
from enum import Enum


class TicTacToeStateType(Enum):
    NOT_PLAYING = 1
    LOBBYING = 2
    PLAYING = 3


ticTacToeState = TicTacToeStateType.NOT_PLAYING
ticTacToePlayers = []
ticTacToeTurn = 0
ticTacToeBoard = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


@commands.command()
async def tictactoe(ctx, arg1=''):
    ctx.send('Work in progress.')

    '''
    global ticTacToeState, ticTacToePlayers, ticTacToeTurn, ticTacToeBoard

    if ticTacToeState == TicTacToeStateType.NOT_PLAYING:
        # start lobbying
        await ctx.send(f"{ctx.author.display_name} has joined as Player 1!")
        await ctx.send("Awaiting one more player in the lobby.")
        ticTacToeState = TicTacToeStateType.LOBBYING
        ticTacToePlayers.insert(ctx.author)
        return

    if ticTacToeState == TicTacToeStateType.LOBBYING:
        # keep lobbying
        if arg1 == 'stop':
            await ctx.send("Disbanding lobby now...")
            ticTacToeState = TicTacToeStateType.NOT_PLAYING
            ticTacToePlayers.clear
            return

        await ctx.send(f"{ctx.author.display_name} has joined as Player 2!")
        await ctx.send("Max players reached. Starting game now!")
        ticTacToeState = TicTacToeStateType.PLAYING
        ticTacToePlayers.insert(ctx.author)
        ticTacToeTurn = 0
        return

    if ticTacToeState == TicTacToeStateType.PLAYING:
        # end the game
        if arg1 == 'stop':
            await ctx.send("Ending game now...")
            ticTacToeState = TicTacToeStateType.NOT_PLAYING
            ticTacToePlayers.clear
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


def setup(bot):
    # Every extension should have this function
    bot.add_command(tictactoe)
