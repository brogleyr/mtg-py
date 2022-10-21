
class Deck:
    cards = []
    def __init__(self, cards):
        self.cards = cards

    def is_legal(self):
        if len(self.cards) < self.minimum_deck_size:
            print(self.cards)
            raise Exception('Not enough cards in deck')
        name_restricted_cards = self.cards
        if not self.basic_land_restriction:
            restricted_filter = filter(
                lambda c: not c.is_basic_land(), self.cards
            )
            name_restricted_cards = []
            for i in restricted_filter:
                name_restricted_cards.append(i)
        card_counts = [name_restricted_cards.count(card) for card in name_restricted_cards]
        max_count = max(card_counts)
        if max_count > self.same_name_restriction:
            raise Exception('Deck has too many of some card')
        return True

class ConstructedDeck(Deck):
    # 100.2a 
    minimum_deck_size = 60
    basic_land_restriction = False
    same_name_restriction = 4

class LimitedDeck(Deck):
    # 100.2b 
    minimum_deck_size = 40
    basic_land_restriction = False
    same_name_restriction = False

class CommanderDeck(Deck):
    # 100.2c - See rule 903, “Commander,” for details
    pass

class SupplementaryDeck(Deck):
    # 100.2d see rule 108.2a, 718, 901, 904
    pass