from random import shuffle
from card import Card


class Shoe():

	""" A shoe of cards made out of a number of traditional decks.  User will
	be asked for the number of decks to put in the shoe.

	Arguments
	---------
	num_decks : int 
		The number of decks supplied by the user.
		Defaults to 1 deck.

	Parameters
	----------
	cards : list
		A list of the cards currently available to the players
	suits : list
		A list of strings reprsenting the 4 suits possible in a deck
	__len__ : built-in (overloaded)
		

	"""

	def __init__(self, num_decks=1):
		self.num_decks = num_decks
		self.cards = self.constructor()

	def __len__(self):
		""" Overloading Builtin: Assigns the value of len(list of cards) to the
		length of the object
		"""
		return len(self.cards)


	def constructor(self):
		""" Builds a shoe of playing card decks.  Each card in a given deck
			will be unique.

		Returns
		-------
		list
			A list of cards that is a (num_decks) multiple of standard
			52 card decks.
		"""
		suits = ['H', 'D', 'C', 'S']
		possible_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J',
						  'Q', 'K', 'A']
		return [Card((c, elem)) for elem in suits for c in possible_cards for i\
				in range(self.num_decks)]


	def shuffle_shoe(self):
		""" Shuffles the order of the cards in the list that constitues the
		shoe.
		"""
		shuffle(self.cards)

	def hand_out_card(self):
		""" Takes the top card, aka the last card in the list of cards and
		removes it from the list and returns it.
		"""
		if self.cards:
			return self.cards.pop()
		else:
			return False

	def merge_sort(self): # , lst=self.cards):
		# """ Sorts the remaining cards from highest to lowest using the merge
		# sort algorithm
		# """
		# sort_list = list(lst)
		# mid = len(sort_list) // 2 # To split the list roughly in half
		# sort_list[:mid] sort_list[mid:]
		pass