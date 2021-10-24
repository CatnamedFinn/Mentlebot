import discord
import os

from discord.ext import commands


token = os.environ.get('DISCORD_TOKEN')
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

#yo like the keywords
keywords = {
    'genshin': 'impact',
    'phoenix': 'boss does it',
    'so true': 'bestie',
    'so untrue': 'worstie',
    'danta': 'SUNNY OMORI'
}


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
    
    #yo like the keyword execution
    for key, value in keywords.items():
        if key in content.lower():
            await message.channel.send(f"Yo, like the {value}?")

    
  

# Path to the file, instead of using a slash use a period
bot.load_extension("commands.almond")
bot.load_extension("commands.susfinder")
bot.load_extension("commands.ticTacToe")
bot.load_extension("commands.about")
bot.load_extension("command.partymanager")


bot.run(token)
