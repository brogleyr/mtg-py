from src.mtg import Game
from src.player import Player
from src.deck import Deck
from assets.sample_decks import *

tmb = Deck(too_many_bears)
jrb = Deck(just_right_bears)
nec = Deck(not_enough_cards)

nick = Player('nick', jrb)
amy = Player('amy', jrb)

game = Game([nick, amy], 'constructed')
game.are_decks_legal()