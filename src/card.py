# 100.2a 
class Card:
    name = ''
    card_type = ''

    # 100.3
    special_designation = None
    nontraditional = False

    def __init__(self, name, card_type='') -> None:
        self.name = name
        self.card_type = card_type

    # 100.2a see rule 201.3
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.name == other.name
        return False

    def __repr__(self):
        return self.name
    
    def is_basic_land(self) -> bool:
        return 'basic land' in self.card_type