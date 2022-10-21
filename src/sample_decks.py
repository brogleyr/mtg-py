from card import Card
too_many_bears = []
for i in range(24):
    too_many_bears.append(Card( 'forest', 'basic land'))
for i in range (36):
    too_many_bears.append(Card('grizzly bears'))

just_right_bears = []
for i in range(60):
    just_right_bears.append(Card( 'forest', 'basic land'))
for i in range (4):
    just_right_bears.append(Card('grizzly bears'))

not_enough_cards = []
for i in range(59):
    not_enough_cards.append(Card( 'forest', 'basic land'))