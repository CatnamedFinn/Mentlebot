import discord
from discord.ext import commands
from main import DAILY_MONEY, members


@commands.command()
async def e(ctx, action):
    author = ctx.author
    author_id_str = f'{author.id}'

    member = members[author_id_str]

    if member == None:
        new_member_name = author.display_name
        members[author_id_str] = {
            'name': new_member_name,
            'money': 0,
            'has_claimed': False,
            'todo': [],
            'inventory': [],
        }
        await ctx.send(f"Hello, {new_member_name}! You have successfully been registered.")
        return

    if action == 'bank':
        await ctx.send(f"Hello, {member['name']}. You currently have {member['money']} $C in your account.")
        return

    if action == 'claim':
        if member['has_claimed'] == False:
            await ctx.send(f"Good day, {member['name']}! Here is your daily {DAILY_MONEY} $C!")
            members[author_id_str]['has_claimed'] = True
        else:
            await ctx.send("You have claimed your $C for today.")
        return

    await ctx.send("Do you want to check your `bank` or `claim`?")


def setup(parent_bot):
    # Every extension should have this function
    parent_bot.add_command(e)
