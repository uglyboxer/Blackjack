class Player:
	""" The hand of cards for a given player 
	
	Arguments
	---------
	shoe : Instance of Shoe Class
		The current shoe initialized in Blackjack.sitting()

	Parameters
	----------
	hand_of_cards : list
		A list of cards in the current hand.
	max_target_score : int
		A constant set to 21 per the rules of blackjack
	interested : bool
		Represents whether the player is still interested in more cards during
		the turn or not.
	"""

	def __init__(self, shoe):
		self.shoe = shoe
		self.hand_of_cards = []
		self.max_target_score = 21
		self.interested = True

	def score(self):
		""" Calculates the current score of the hand """

		total = sum([card.value for card in self.hand_of_cards])
		if total > self.max_target_score:
			for card in self.hand_of_cards:
				if card.value == 11:
					card.flip_ace()
					total = sum([card.value for card in\
								 self.hand_of_cards])
					break	# So only one ace gets flipped.
		return total

	def pretty_output(self):
		""" Creates a string of the current cards for output """
		full_hand = ""
		for card in self.hand_of_cards:
			full_hand += card.card_name + " "
		return full_hand

	def get_card(self):
		""" Gets a new card from the shoe """
		if self.shoe.cards:
			self.hand_of_cards.append(self.shoe.hand_out_card())
			return True
		else:
			return False

class Dealer(Player):
	""" A subclass of the class Player, with a method to determine if he hits
	or not in a given situation.
	"""

	def hits(self):
		if self.score() < 17:
			return True
		else:
			self.interested = False
			return False


class User(Player):
	""" A subclass of the class Player, with a method to determine if he hits
	or not in a given situation.
	"""

	def hits(self):
		choice = input("Would you like another card? (y/n) ")
		print("\n")
		if choice.lower().strip() == 'y':
			return True
		else:
			self.interested = False
			return False