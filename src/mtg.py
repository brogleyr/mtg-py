
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
    
    def start(self):
        for player in self.players:
            if self.game_type == 'constructed':
                player.deck = ConstructedDeck(player.deck.cards)
            elif self.game_type == 'limited':
                player.deck = LimitedDeck(player.deck.cards)
            elif self.game_type == 'commander':
                player.deck = CommanderDeck(player.deck.cards)
            else:
                raise Exception('No legal game type selected')
            
            if not player.deck.is_legal():
                raise Exception('A player\'s deck was not legal')
        print('Both decks look good, let\'s begin')

