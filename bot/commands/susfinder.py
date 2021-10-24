import discord
import re

from discord.ext import commands


@commands.command()
async def susfinder(ctx):
    message = ctx.message

    if message.reference is None:
        await ctx.send("You need to reply to a message in order to sussify it.")
        return

    reply_id = message.reference.message_id
    reply = await ctx.channel.fetch_message(reply_id)
    content = reply.content

    sussified = re.sub("[^s.*u.*s]", "█", content)
    await ctx.send(sussified)


def setup(bot):
    # Every extension should have this function
    bot.add_command(susfinder)
