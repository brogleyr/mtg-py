# 100.2a 
class Card:
    name = ''
    card_type = ''
    def __init__(self, name, card_type=''):
        self.name = name
        self.type = card_type

    # 100.2a see rule 201.3
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.name == other.name
        return False

    def __repr__(self):
        return self.name
    
    def is_basic_land(self):
        return 'basic land' in self.type