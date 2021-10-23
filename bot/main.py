import discord
import os

token = os.environ.get('DISCORD_TOKEN')
client = discord.Client()


async def fuck_detector(message):
    await message.channel.send("Woah")


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!hello"):
        await message.channel.send("Hello")
    if message.content("shit"):
        fuck_detector(message)

client.run(token)
