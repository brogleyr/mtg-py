
class Deck:
    cards = []
    def __init__(self, cards):
        self.cards = cards
        if hasattr(self, 'minimum_deck_size') and not self.meets_minimum_card_req():
            raise Exception('deck has too few cards')
        if hasattr(self, 'same_name_restriction') and not self.meets_card_name_restriction():
            raise Exception('deck has too many of a card')

    def meets_minimum_card_req(self):
        return len(self.cards) >= self.minimum_deck_size

    def meets_card_name_restriction(self):
        name_restricted_cards = self.cards
        if not self.basic_land_restriction:
            restricted_filter = filter(
                lambda c: not c.is_basic_land(), self.cards
            )
            name_restricted_cards = []
            for i in restricted_filter:
                name_restricted_cards.append(i)

        card_counts = [
            name_restricted_cards.count(card) for card in name_restricted_cards
        ]
        max_count = max(card_counts)
        return max_count <= self.same_name_restriction

class ConstructedDeck(Deck):
    # 100.2a 
    minimum_deck_size = 60
    basic_land_restriction = False
    same_name_restriction = 4

    def __init__(self, deck):
        super().__init__(deck.cards)
        

class LimitedDeck(Deck):
    # 100.2b 
    minimum_deck_size = 40
    basic_land_restriction = False
    same_name_restriction = False

    def __init__(self, deck):
        super().__init__(deck.cards)

class CommanderDeck(Deck):
    # 100.2c - See rule 903, “Commander,” for details
    def __init__(self, deck):
        super().__init__(deck.cards)

class SupplementaryDeck(Deck):
    # 100.2d see rule 108.2a, 718, 901, 904
    def __init__(self, deck):
        super().__init__(deck.cards)