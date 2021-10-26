import discord
from discord.ext import commands
import re

@commands.command()
async def fx(ctx):
    message = ctx.message
    
    if message is None:
        await ctx.send("You need to reply to a message.")
        return
    
    reply_id = message.reference.message_id
    reply = await ctx.channel.fetch_message(reply_id)
    text = reply.content

    


    