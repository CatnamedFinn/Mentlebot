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
async def sussify(ctx):
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
        ticTacToeState = TicTacToeStateType.LOBBYING
        ticTacToePlayers.insert(ctx.author)
        return

    if ticTacToeState == TicTacToeStateType.LOBBYING:
        # keep lobbying
        if arg1 == 'stop':
            await ctx.send("Aborting game now...")
            ticTacToeState = TicTacToeStateType.NOT_PLAYING
            ticTacToePlayers.clear
            return

        playerCount = len(ticTacToePlayers)
        ticTacToePlayers.insert(ctx.author)
        await ctx.send(f"{ctx.author.display_name} has joined as Player {playerCount}!")

        if playerCount == 2:
            await ctx.send("Max players reached. Starting game now!")
            ticTacToeState = TicTacToeStateType.PLAYING
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
async def about(ctx):
    embed = discord.Embed(title = "What the frick is Mentlebot?", description = "Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color = discord.Color.blurple())
    
    embed.set_thumbnail(url = "https://preview.redd.it/jpzji9ml0rq71.jpg?auto=webp&s=b005458162a35f0275d7edf8f5b15e7617efd983")

    embed.add_field(name = "Features", value = "Below are the list of commands I can perform.", inline = False)
    embed.add_field(name = "WD Ghost-Free", value = "Anti ghosting feature. Members @'ed within the command must reply to the original message or be greeted with an n number of messages and @s from the bot. The message contents and the number of messages sent can be configured.", inline = True)
    embed.add_field(name = "Party manager" , value = "Game party tracking feature. @s a party role and tracks the number of subscribed members that replied to the @, closing the original @ once the maximum number of members replying to it is met. Party role and maximum number of members can be configured." , inline = True)
    embed.add_field(name = "Stuffify" , value = "Creates and sends an 'I'm Stuff' macro meme with custom text.", inline = True)
    embed.add_field(name = "Adit", value = "Command that sends a DM and/or @s the member 'Adit'", inline = True)
    embed.add_field(name = "Adit.int", value = "Posts a picture of the member 'Adit' inting or feeding. Gallery for said pictures is available at ___.", inline = True)
    embed.add_field(name = "Team.int", value = "Posts a picture of an entire team inting or feeding. Gallery for said pictures is available at ___.", inline = True)
    embed.add_field(name = "4k", value = "Posts an extremely sus picture. Gallery for said pictures is available at ___.", inline = True)
    embed.add_field(name = "Yo like the?", value = "Custom automatic reply feature. The bot replies to a message containing a custom keyword with 'You like the <custome message>'.", inline = True)
    embed.add_field(name = "Susfinder", value = "Replies to the command message with a message containing only the characters 's', 'u', and 's' in order.", inline = True)
    embed.add_field(name = "Tic tac toe", value = "I'm pretty sure you know what this is.", inline = True)

    embed.set_footer(text = "This is a personal project so don't take this seriously.")
    
    await ctx.send(embed = embed)


bot.run(token)
