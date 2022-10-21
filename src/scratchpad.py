from mtg import Card

gb = Card('grizzly bear')
f = Card('forest', 'basic land')

print(gb.is_basic_land())
print(f.is_basic_land())