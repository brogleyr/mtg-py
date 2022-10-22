
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
            try:
                player.set_game_type(self.game_type)
            except Exception as e:
                return False
        return True

