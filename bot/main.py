import discord
import os

token = os.environ.get('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!hello"):
        await message.channel.send("Hello")
    

@client.event
async def fuck_detector(message):
    if message.author == client.user:
        return
    await message.channel.send(message.replace("fuck", ""))

client.run(token)
