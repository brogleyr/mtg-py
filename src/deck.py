
from typing import List
from src.card import Card

class Deck:
    cards: List[Card] = []
    maximum_deck_size: int = 0
    minimum_deck_size: int = 0
    basic_land_restriction: bool = False
    same_name_restriction: int = 0


    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards
        if not self.meets_minimum_card_req():
            raise Exception('deck has too few cards')
        if not self.meets_card_name_restriction():
            raise Exception('deck has too many of a card')

    def meets_minimum_card_req(self):
        if self.minimum_deck_size:
            return len(self.cards) >= self.minimum_deck_size
        return True

    def meets_maximum_card_req(self):
        if self.maximum_deck_size:
            return len(self.cards) <= self.maximum_deck_size
        return True

    def meets_card_name_restriction(self):
        if not self.same_name_restriction:
            return True
        limited_copies = self.cards
        if not self.basic_land_restriction:
            restricted_filter = filter(
                lambda c: not c.is_basic_land(), limited_copies
            )
            limited_copies = [card for card in restricted_filter]

        card_counts = [
            limited_copies.count(card) for card in limited_copies
        ]
        max_count = max(card_counts)
        return max_count <= self.same_name_restriction

class ConstructedDeck(Deck):
    # 100.2a 
    minimum_deck_size = 60
    basic_land_restriction = False
    same_name_restriction = 4

    def __init__(self, deck: Deck):
        super().__init__(deck.cards)
        
class LimitedDeck(Deck):
    # 100.2b 
    minimum_deck_size = 40
    basic_land_restriction = False
    same_name_restriction = False

    def __init__(self, deck: Deck):
        super().__init__(deck.cards)

# 100.2c - See rule 903, “Commander,” for details
class CommanderDeck(Deck):
    # 100.5
    maximum_deck_size: int = 0


    def __init__(self, deck: Deck):
        super().__init__(deck.cards)

class SupplementaryDeck(Deck):
    # 100.2d see rule 108.2a, 718, 901, 904
    def __init__(self, deck: Deck):
        super().__init__(deck.cards)

#100.4
class Sideboard(Deck):
    cards: List[Card] = []
    maximum_deck_size: int = 0
    same_name_restriction: bool = 0

    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards
        if not self.meets_maximum_card_req():
            raise Exception('sideboard has too many cards')

    def meets_maximum_card_req(self):
        if self.maximum_deck_size:
            return len(self.cards) <= self.maximum_deck_size
        return True

# 100.4a 
class ConstructedSideboard(Sideboard):
    maximum_deck_size: int = 15
    same_name_restriction: int = 4

    def __init__(self, sideboard: Sideboard):
        super().__init__(sideboard.cards)


# 100.4b
class LimitedSideboard(Sideboard):

    def __init__(self, sideboard: Sideboard):
        super().__init__(sideboard.cards)

# 100.4c 
class TwoHeadedGiantSideboard(Sideboard):
    pass


# 100.4b 
class CardPool():
    deck: Deck = None
    sideboard: Sideboard = None
    game_type: str = None

    def __init__(self, deck: Deck|List[Card], sideboard:Sideboard|List[Card] = None):
        if type(deck) is Deck:
            self.deck = deck
        else:
            self.deck = Deck(deck)
        if sideboard:
            if type(sideboard) is Sideboard:
                self.sideboard = sideboard
            else:
                self.sideboard = Sideboard(sideboard)

    def set_game_type(self, game_type: str):
        self.game_type = game_type
        if game_type == 'constructed':
            self.deck = ConstructedDeck(self.deck)
            if self.sideboard:
                self.sideboard = ConstructedSideboard(self.sideboard)
        elif game_type == 'limited':
            self.deck = LimitedDeck(self.deck)
            if self.sideboard: 
                self.sideboard = LimitedSideboard(self.sideboard)
        elif game_type == 'commander':
            self.deck = CommanderDeck(self.deck)
        else:
            raise Exception('no game type selected')
        if not self.meets_card_name_restriction():
            raise Exception('card pool has too many of a card')
        return True

    def meets_card_name_restriction(self) -> bool:
        if not self.deck.same_name_restriction:
            return True
        limited_copies = self.deck.cards
        if self.sideboard:
            limited_copies.extend(self.sideboard.cards)
        if not self.deck.basic_land_restriction:
            restricted_filter = filter(
                lambda c: not c.is_basic_land(), limited_copies
            )
            limited_copies = [card for card in restricted_filter]

        card_counts = [
            limited_copies.count(card) for card in limited_copies
        ]
        max_count = max(card_counts)
        return max_count <= self.deck.same_name_restriction

    def get_deck(self) -> Deck:
        return self.deck

    def set_deck(self, deck: Deck) -> None:
        self.deck = deck

    def get_sideboard(self) -> Sideboard:
        return self.sideboard

    def set_sideboard(self, sideboard: Sideboard) -> None:
        self.sideboard = sideboard

# 100.4c 
class THGCardPool(CardPool):
    deck: List[Deck] = []
    sideboard: Sideboard = None

# 100.4d
class TeamCardPool(CardPool):
    deck: List[Deck] = []
    #Cards cannot transfer between sideboards
    sideboard: List[Sideboard] = []
