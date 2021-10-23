import discord
import os

from discord.ext import commands

token = os.environ.get('DISCORD_TOKEN')
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


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
async def about(ctx, arg=0):
    arg = int(arg)
    await ctx.send(arg)
    if arg == 1:
        embed = discord.Embed(
            title="WD Ghost Free", description="Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color=discord.Color.blurple())
    elif arg == 2:
        embed = discord.Embed(
            title="Stuffify", description="Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color=discord.Color.blurple())
    elif arg == 3:
        embed = discord.Embed(
            title="Adit", description="Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color=discord.Color.blurple())
    elif arg == 4:
        embed = discord.Embed(
            title="Adit.int", description="Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color=discord.Color.blurple())
    elif arg == 5:
        embed = discord.Embed(
            title="Team.int", description="Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color=discord.Color.blurple())
    elif arg == 6:
        embed = discord.Embed(
            title="4K", description="Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color=discord.Color.blurple())
    elif arg == 7:
        embed = discord.Embed(
            title="Yo like the?", description="Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color=discord.Color.blurple())
    elif arg == 8:
        embed = discord.Embed(
            title="Susfinder", description="Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color=discord.Color.blurple())
    elif arg == 9:
        embed = discord.Embed(
            title="Tic Tac toe", description="Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color=discord.Color.blurple())
    else:
        embed = discord.Embed(title="What the frick is Mentlebot?",
                              description="Hello fellow user, I am Mentlebot, a joint project between two IT random furries made with the goal for coding practice and fun.", color=discord.Color.blurple())

        embed.set_thumbnail(
            url="https://preview.redd.it/jpzji9ml0rq71.jpg?auto=webp&s=b005458162a35f0275d7edf8f5b15e7617efd983")

        embed.add_field(
            name="Features", value="Below are the list of commands I can perform.", inline=False)
        embed.add_field(name="1) WD Ghost-Free",
                        value="Anti ghosting feature.", inline=True)
        embed.add_field(name="2) Party manager",
                        value="Game party tracking feature.", inline=True)
        embed.add_field(name="3) Stuffify",
                        value="Posts custom 'I'm stuff' images", inline=True)
        embed.add_field(name="4) Adit",
                        value="@s or DMs the member 'Adit'", inline=True)
        embed.add_field(name="5) Adit.int",
                        value="Posts a picture of Adit inting or feeding", inline=True)
        embed.add_field(name="6) Team.int",
                        value="Posts a picture of an entire team inting or feeding.", inline=True)
        embed.add_field(name="7) 4k",
                        value="Posts an extremely sus picture.", inline=True)
        embed.add_field(name="8) Yo like the?",
                        value="Bot responds to a keyword with a custom message.", inline=True)
        embed.add_field(name="9) Susfinder",
                        value="Highlights 's', 'u' and 's' in a message", inline=True)
        embed.add_field(name="10) Tic tac toe",
                        value="I'm pretty sure you know what this is.", inline=True)

    await ctx.send(embed=embed)

# Path to the file, instead of using a slash use a period
bot.load_extension("commands.almond")
bot.load_extension("commands.susfinder")
bot.load_extension("commands.ticTacToe")
bot.run(token)
