import discord
from discord.ext import commands

roles = {
    '@lolplayers': 5
}
lobby = []

@commands.command()
async def party2(ctx, role = None, maxPlayers = 0):
    #if the member does not input anything after command
    if role == None and maxPlayers == 0: 
        await ctx.send("Checkpoint 1")    
    #initiating a lobby
    elif role in roles.keys(): 
        await ctx.send("Checkpoint 2")  
        if len(lobby) == 0: 
            lobby.append(ctx.author.display_name)
            await ctx.send(f"{ctx.author.mention} wants to play {role}. {len(lobby)}/{roles.get(role)}." )
        #allowing people to join the lobby
        elif len(lobby) < 5: 
            if ctx.author.display_name in lobby:
                await ctx.send("You're already in the lobby!")
                return
            lobby.append(ctx.author.display_name)
            await ctx.send(f"{ctx.author.mention} has joined. {len(lobby)}/{roles.get(role)}." )
            if len(lobby) == 5:
                temp = ''
                for item in lobby:
                    temp += f" {item}, "
                await ctx.send(f"Max players reached. Players are{temp}")
                lobby.clear()
    elif role != None and maxPlayers > 1:
        await ctx.send("Checkpoint 3")  
        if '@' not in role: 
           await ctx.send("Please mention a role.")
        roles[role] = maxPlayers
        await ctx.send(f"list of roles has been updated. Current party roles are: {roles.items()}.")

def setup(bot):
    # Every extension should have this function
    bot.add_command(party2)
