from mtg import Game
from player import Player
from deck import Deck
from sample_decks import *

tmb = Deck(too_many_bears)
jrb = Deck(just_right_bears)
nec = Deck(not_enough_cards)

nick = Player(just_right_bears)
amy = Player(just_right_bears)

game = Game([nick, amy], 'constructed')
game.start()