
from src.deck import *
from src.player import Player

class Game:
    players: List[Player] = []
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
            player_cards = player.get_cardpool()
            cards_are_legal = player_cards.set_game_type(self.game_type)
            if not cards_are_legal:
                print('{}\'s deck was not legal'.format(player.name))
                return False
        return True

