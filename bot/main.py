import discord

client = discord.Client()

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

client.run("OTAwOTk2MDk0MDg1OTc2MDc2.YXJcAA.vlgFeBnER7dsd5GjFznP3vP09Q8")
