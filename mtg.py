
class Game:

    def __init__(self, num_players):
        self.players = []
        for i in range(num_players):
            self.players.append(Player())

        if num_players == 2:
            self.player_type = "two-player"
        elif num_players > 2:
            self.player_type = "multiplayer"

class Player:
    pass

