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

    embed.set.footer(text = "This is a personal project so don't take this seriously.")
    
    await ctx.send(embed = embed)


bot.run(token)
