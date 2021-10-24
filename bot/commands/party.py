import discord
import re

from discord.ext import commands


games = {
    'lol': {
        'max_players': 5,
        'lobbies': [],
    },
    'genshin': {
        'max_players': 4,
        'lobbies': [],
    },
}


@commands.command(name='game')
async def party(ctx, action='', game=''):
    def find_in_lobby(id='', name=''):
        '''
            If user is in a lobby, returns a LobbyStatus.\n
            LobbyStatus:\n
                game: The lobby's game\n
                game_data: The game object\n
                role: Whether the user initiated this lobby or is participating in it\n
                lobby: The lobby object the user is in\n
            Otherwise, returns None.
        '''
        for game, game_data in games.items():
            lobbies = game_data['lobbies']

            if len(lobbies) == 0:
                return None

            for lobby in lobbies:
                initiator = lobby['initiator']
                if id == initiator['id'] or name == initiator['name']:
                    return {
                        'game': game,
                        'game_data': game_data,
                        'role': 'initiator',
                        'lobby': lobby,
                    }
                for member in lobby['party']:
                    if id == member['id'] or name == member['name']:
                        return {
                            'game': game,
                            'game_data': game_data,
                            'role': 'participator',
                            'lobby': lobby,
                        }
        return None

    commander_id = ctx.author.user_id
    commander_name = ctx.author.displayed_name

    lobby_status = find_in_lobby(id=commander_id)
    await ctx.send(lobby_status)

    if action == 'disband':
        # check if the user is initiating a lobby
        if lobby_status == None or lobby_status['role'] != 'initiator':
            await ctx.send("You don't have an active game lobby!")
            return

        lobbied_game = lobby_status['game']
        lobby_to_pop = lobby_status['lobby']

        party_list = ''
        for member in lobby_to_pop['party']:
            party_list += f" @{member['name']}, "

        lobbies = games[lobbied_game]['lobbies']
        lobbies = [i for i in lobbies if i['initiator']['id'] != commander_id]

        await ctx.send(f"Disbanding your {game} lobby containing:{party_list}")
        return

    if action == 'leave':
        # check if user is in a lobby
        if lobby_status == None:
            await ctx.send("You're not participating in a game lobby!")
            return
        if lobby_status['role'] == 'initiator':
            await ctx.send(
                "You can't leave if you're initiating a game lobby! "
                "Disband your lobby instead using `!party disband`")
            return

        lobbied_game = lobby_status['game']
        lobbied_game_data = lobby_status['game_data']
        lobby = lobby_status['lobby']

        initiator = lobby['initiator']
        party = lobby['party']

        party = [i for i in party if i['id'] != commander_id]

        await ctx.send(
            f"{commander_name} has left {initiator['name']}'s {lobbied_game} lobby. "
            f"**({len(party) + 1} / {lobbied_game_data['max_players']})**")
        return

    if action == 'create':
        # check if user is in a lobby
        if lobby_status != None:
            if lobby_status['role'] == 'initiator':
                await ctx.send(
                    "You're already initiating a pre-existing lobby! "
                    "Disband your current lobby first using `!party disband`")
                return
            else:
                await ctx.send(
                    "You're already participating in another lobby! "
                    "Leave your current lobby first using `!party leave`")
                return

        # param check
        if game == '':
            await ctx.send("You need to specify what `game` lobby you want to initiate.")
            return
        if game not in games.keys():
            game_list = ''
            for game in games.keys():
                game_list += f" `{game}`"

            await ctx.send(
                "We couldn't find your game in the registered list. Please contact the Gazza about this. "
                f"Here are all the registered games:{game_list}")
            return

        game_data = games[game]
        game_data['lobbies'].insert(
            {
                'initiator': {
                    'name': commander_name,
                    'id': commander_id,
                },
                'party': [],
            }
        )
        await ctx.send(
            f"@{commander_name} has created a {game} lobby! Join them y'all. **(1 / {game_data['max_players']})**")
        return

    if action == 'join':
        # check if user is in a lobby
        if lobby_status != None:
            if lobby_status['role'] == 'initiator':
                await ctx.send(
                    "You're already initiating a pre-existing lobby! "
                    "Disband your current lobby first using `!party disband`")
                return
            else:
                await ctx.send(
                    "You're already participating in another lobby! "
                    "Leave your current lobby first using `!party leave`")
                return

        # check reply
        message = ctx.message

        if message.reference is None:
            await ctx.send("You need to reply to a lobby announcement in order to join a game.")
            return

        reply_id = message.reference.message_id
        reply = await ctx.channel.fetch_message(reply_id)

        parsed = re.search("@(.+) has created a (.+) lobby!", reply.content)
        if parsed == None:
            await ctx.send("That doesn't look like a lobby announcement to me.")
            return

        initiator = parsed.group(1)
        lobby_status = find_in_lobby(name=initiator)

        if lobby_status == None or lobby_status['role'] != 'initiator':
            await ctx.send(
                "That user doesn't seem to be initiating a lobby at the moment. "
                "They may have disbanded the one in my announcement.")
            return

        lobbied_game = lobby_status['game']
        lobbied_game_data = lobby_status['game_data']
        lobbied_game_max_players = lobbied_game_data['max_players']

        lobby = lobby_status['lobby']
        party = lobby['party']
        party_size = len(party)

        if party_size == lobbied_game_max_players:
            await ctx.send(
                "This lobby is full.")
            return

        party.insert({
            'name': commander_name,
            'id': commander_id,
        })
        party_size = len(party)

        await ctx.send(
            f"@{commander_name} has joined {initiator}'s {game} lobby! **({party_size + 1} / {lobbied_game_max_players})**")

        if party_size == lobbied_game_max_players:
            await ctx.send(
                f"{initiator}'s {lobbied_game} lobby is now full! Not accepting any more joins. "
                "Don't forget to disband this lobby after you're finished.")
            return

    await ctx.send(
        "You need to specify what you want to do. "
        "Either `create` `join` `leave` or `disband`")


def setup(bot):
    # Every extension should have this function
    bot.add_command(party)
