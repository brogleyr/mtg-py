from deck import Deck

# 100.2
class Player:
    life_total = 0
    deck = None

    def __init__(self, name, deck):
        self.name = name
        self.deck = deck

    def __repr__(self):
        return self.name