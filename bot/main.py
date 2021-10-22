import discord
import os

client = discord.Client()

token = os.environ.get('BOT_TOKEN')

@client.event
async def onReady():
    print("We have logged in as {0.user}".format(client))
    
@client.event
async def onMessage(message):
    if message.author == client.user:
        return
    fuckDetector(message)
    if message.content.startswith("!hello"):
        await message.channel.send("Hello")
    

@client.event
async def fuckDetector(message):
    await message.channel.send(message.replace("fuck", ""))

client.run(token)
