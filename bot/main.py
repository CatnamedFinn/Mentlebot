import discord
import os
import re

from discord.ext import commands


token = os.environ.get('DISCORD_TOKEN')
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# yo like the keywords
keywords = {
    'genshin': 'impact',
    'phoenix': 'boss does it',
    'so true': 'bestie',
    'so untrue': 'worstie',
    'danta': 'SUNNY OMORI',
    'super': 'Idol的笑容 都没你的甜 八月正午的阳光 都没你耀眼 热爱 105 °C的你 滴滴清纯的蒸馏水'
}


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.event
async def on_message(message):
    author = message.author
    content = message.content

    if author == bot.user:
        return
    if author.bot == True:
        return

    # funny emoji
    message.add_reaction('💩')

    # yo like the keyword execution
    for key, value in keywords.items():
        if key in content.lower():
            await message.channel.send(f"Yo, like the {value}?")

    # fx twitter link converter
    twitter_post_match = re.match(
        "(https:\/\/)(twitter.com\/[a-zA-Z0-9]+\/status\/[0-9]+)", content)
    if twitter_post_match != None:
        op = f"Originally sent by {author.mention}"
        await message.channel.send(f"{op}\n{twitter_post_match.group(1)}fx{twitter_post_match.group(2)}")
        await message.delete()

    await bot.process_commands(message)


# Path to the file, instead of using a slash use a period
bot.load_extension("commands.almond")
bot.load_extension("commands.bologna")

bot.load_extension("commands.about")
bot.load_extension("commands.partymanager")

bot.load_extension("commands.party")
bot.load_extension("commands.susfinder")
bot.load_extension("commands.tictactoe")

bot.load_extension("commands.testMention")

bot.load_extension("commands.fxregex")


bot.run(token)
