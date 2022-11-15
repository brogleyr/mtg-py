from src.mtg import Game
from src.player import Player
from src.deck import Deck, Sideboard
from assets.sample_decks import *

tmb = Deck(too_many_bears)
jrb = Deck(just_right_bears)
nec = Deck(not_enough_cards)
tbd = Deck(two_bears_deck)

bs = Sideboard(big_sideboard)
m4s = Sideboard(more_than_four_sideboard)
tbs = Sideboard(two_bears_sideboard)

nick = Player('nick', tbd, tbs)
amy = Player('amy', tbd, tbs)

game = Game([nick, amy], 'constructed')
if game.are_decks_legal():
    print('Both decks look good')
else:
    print('There were deck errors')