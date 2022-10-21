
import sys
from deck import *

class Game:
    players = []
    # 100.1.
    def __init__(self, players, game_type):
        self.players = players
        # 100.1a
        if len(players) == 2:
            self.player_type = 'two-player'
        # 100.1b
        elif len(players) > 2:
            self.player_type = 'multiplayer'

        self.game_type = game_type
    
    def are_decks_legal(self):
        for player in self.players:
            try:
                if self.game_type == 'constructed':
                    player.deck = ConstructedDeck(player.deck)
                elif self.game_type == 'limited':
                    player.deck = LimitedDeck(player.deck)
                elif self.game_type == 'commander':
                    player.deck = CommanderDeck(player.deck)
                else:
                    print('No game type selected')
                    return False
            except Exception as e:
                print(f'{player}\'s {e}')
                return False

        print('Both decks look good')
        return True

