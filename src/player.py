from deck import Deck

# 100.2
class Player:
    life_total = 0
    deck = None

    def __init__(self, deck):
        self.deck = Deck(deck)