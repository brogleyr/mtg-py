from typing import List
from src.deck import *
from src.card import Card

# 100.2
class Player:
    life_total: int = 0
    card_pool: CardPool = None

    def __init__(
        self,
        name: str,
        deck: Deck|List[Card],
        sideboard:Sideboard|List[Card] = None
    ):
        self.name = name
        self.card_pool = CardPool(deck, sideboard)

    def get_deck(self) -> Deck:
        return self.card_pool.get_deck()

    def get_cardpool(self) -> CardPool:
        return self.card_pool

    def __repr__(self):
        return self.name