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

    lobby_status = find_in_lobby(id=commander_id)
    await ctx.send(lobby_status)
    await ctx.send(
        "You need to specify what you want to do. "
        "Either `create` `join` `leave` or `disband`")


def setup(bot):
    # Every extension should have this function
    bot.add_command(party)
