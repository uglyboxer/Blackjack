""" blackjack.py
Author: Cole Howard

A simple implementation of the game of blackjack.

The user is tasked with defining the number of decks of 52 cards to be used in
the shoe.  The game can then be played until the shoe runs out or the user opts
out.


Dependencies
------------
	Python 3.0 or newer
"""


class Card:
	""" Class of a single card in a traditional deck of 52 cards.
	Cards are 2 - 10 and have a value matching their integer name.
	or the are a 'face' card (Jack, Queen, King) and valued at 10.
	Ace cards are valued at 1 or 11 depending on the state of the rest of the
		hand.
	"""

	def __init__(self):
		self.value = 0

	def assign_value():
		pass

	def flip_ace:
		pass


class Shoe:

	""" A shoe of cards made out of a number of traditional decks.  User will
	be asked for the number of decks to put in the shoe.

	Parameters
	----------
	num_decks : int 
		The number of decks supplied by the user.
		Defaults to 1 deck.

	"""

	def __init__(num_decks=1):
