from src.card import Card

forest = Card('forest', 'basic land')
grizzly_bears = Card('grizzly bears')

too_many_bears = []
for i in range(24):
    too_many_bears.append(forest)
for i in range (36):
    too_many_bears.append(grizzly_bears)

just_right_bears = []
for i in range(60):
    just_right_bears.append(forest)
for i in range (4):
    just_right_bears.append(grizzly_bears)

two_bears_deck = []
for i in range(60):
    two_bears_deck.append(forest)
for i in range(2):
    two_bears_deck.append(grizzly_bears)

not_enough_cards = []
for i in range(59):
    not_enough_cards.append(forest)

big_sideboard = []
for i in range(16):
    big_sideboard.append(forest)

more_than_four_sideboard = []
for i in range(15):
    more_than_four_sideboard.append(grizzly_bears)

two_bears_sideboard = []
for i in range(2):
    two_bears_sideboard.append(grizzly_bears)