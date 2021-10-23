import discord
import os
import re

from discord.ext import commands

token = os.environ.get('DISCORD_TOKEN')
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

tttBoard = [
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
async def sus(ctx):
    message = ctx.message
    replyId = message.reference.message_id
    reply = await ctx.channel.fetch_message(replyId)
    content = reply.content

    await ctx.send(f"Your message is in reply to this one: '{content}'")

    sussified = re.sub("[^s.*u.*s]", "█", content)
    await ctx.send(sussified)


@bot.command(name='3d3t')
async def _3d3t(ctx):
    await ctx.send(
        "```"
        "X | X | O\n"
        "X |   | O\n"
        "O | X | X\n"
        "```"
    )


@bot.command()
async def tortilla(ctx):
    embed = discord.Embed(title = "What the frick is Mentlebot?", description = "Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color = discord.Color.blurple())

    await ctx.send(embed = embed)


bot.run(token)
