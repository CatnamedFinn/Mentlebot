import discord

client = discord.Client()

@client.event
async def onReady():
    print("We have logged in as {0.user}".format(client))

        
    
@client.event
async def onMessage(message):
    if message.author == client.user:
        return
    if message.content.startswith("!hello"):
        await message.channel.send("Hello")
    

client.run("OTAwOTk2MDk0MDg1OTc2MDc2.YXJcAA.lju4yKrgWfvUdwIHCAPCfB2BNzo")
