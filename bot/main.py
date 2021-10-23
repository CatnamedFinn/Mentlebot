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


ticTacToeState = TicTacToeStateType.NOT_PLAYING
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
    if message.author.bot == True:
        return
    content = message.content

    if content.startswith("!ver"):
        await message.channel.send("ver8")
    elif content.startswith("!hi"):
        await message.channel.send("Hello.")
    await bot.process_commands(message)


@bot.command()
async def susfinder(ctx):
    message = ctx.message

    if message.reference is None:
        await ctx.send("You need to reply to a message in order to sussify it.")
        return

    replyId = message.reference.message_id
    reply = await ctx.channel.fetch_message(replyId)
    content = reply.content

    sussified = re.sub("[^s.*u.*s]", "█", content)
    await ctx.send(sussified)


@bot.command(name='3d3t')
async def _3d3t(ctx, arg1, arg2):
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


@bot.command()
async def about(ctx, arg = 0):
    arg = int(arg)
    if arg == 1:
        embed = discord.Embed(title = "WD Ghost Free", description = "All mentioned members must reply to the initial command message within set amount of time or the bot will periodically mention the with increasing frequency. Mentions start of at 1 every 12 hours decreasing by half after every subsequent mention to a minumum of 1 every 5 seconds.", color = discord.Color.blurple())
        
        embed.add_field(name = "Syntax", value = "!wd <your message> <mentioned members>", inline = False)
    elif arg == 2:
        embed = discord.Embed(title = "Stuffify", description = "Creates and posts a 'I'm Stuff' macro meme with custom text", color = discord.Color.blurple())
        
        embed.add_field(name = "Syntax", value = "!stuffify <custom text>", inline = False)
    elif arg == 3:
        embed = discord.Embed(title = "Adit", description = "Mentions and DMs Adit", color = discord.Color.blurple())

        embed.add_field(name = "Syntax", value = "!adit", inline = False)
    elif arg == 4:
        embed = discord.Embed(title = "Adit.int", description = "Posts a picture of Adit inting or feeding in a game.", color = discord.Color.blurple())

        embed.add_field(name = "Syntax", value = "!adit.int", inline = False)
    elif arg == 5:
        embed = discord.Embed(title = "Team.int", description = "Posts a picture of the entire team inting or feeding in a game.", color = discord.Color.blurple())

        embed.add_field(name = "Syntax", value = "!team.int", inline = False)
    elif arg == 6:
        embed = discord.Embed(title = "4k", description = "Stores discord messages and quotes a random stored message or a random stored message from a specific member.", color = discord.Color.blurple())

        embed.add_field(name = "Syntax", value = "Store message: <reply to message> !4k, quote message: !4k, quote message from specific member: !4k <mention member>", inline = False)
    elif arg == 7:
        embed = discord.Embed(title = "Yo like the?", description = "Bot sends a message starting with 'Yo like the' followed by a custom message when it detects a keyword from a member.", color = discord.Color.blurple())
    elif arg == 8:
        embed = discord.Embed(title = "Susfinder", description = "Redacts a message, leaving only sussy characters", color = discord.Color.blurple())

        embed.add_field(name = "Syntax", value = "<reply to message> !susfinder", inline = False)
    elif arg == 9:
        embed = discord.Embed(title = "Tic Tac toe", description = "I think you know what this is.", color = discord.Color.blurple())

        embed.add_field(name = "Syntax", value = "WIP", inline = False)
    else:
        embed = discord.Embed(title = "What the frick is Mentlebot?", description = "Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color = discord.Color.blurple())

        embed.set_thumbnail(url = "https://preview.redd.it/jpzji9ml0rq71.jpg?auto=webp&s=b005458162a35f0275d7edf8f5b15e7617efd983")

        embed.add_field(name = "Features", value = "Below are the list of commands I can perform.", inline = False)
        embed.add_field(name = "1) WD Ghost-Free", value = "Anti ghosting feature.", inline = True)
        embed.add_field(name = "2) Party manager" , value = "Game party tracking feature." , inline = True)
        embed.add_field(name = "3) Stuffify" , value = "Posts custom 'I'm stuff' images", inline = True)
        embed.add_field(name = "4) Adit", value = "Mentions and DMs the member 'Adit'", inline = True)
        embed.add_field(name = "5) Adit.int", value = "Posts a picture of Adit inting or feeding", inline = True)
        embed.add_field(name = "6) Team.int", value = "Posts a picture of an entire team inting or feeding.", inline = True)
        embed.add_field(name = "7) 4k", value = "Posts an extremely sus picture.", inline = True)
        embed.add_field(name = "8) Yo like the?", value = "Bot responds to a keyword with a custom message.", inline = True)
        embed.add_field(name = "9) Susfinder", value = "Highlights 's', 'u' and 's' in a message", inline = True)
        embed.add_field(name = "10) Tic tac toe", value = "I'm pretty sure you know what this is.", inline = True)
    
    await ctx.send(embed = embed)


bot.run(token)
