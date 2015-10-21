""" blackjack.py
Author: Cole Howard

A simple implementation of the game of blackjack.

The user is tasked with defining the number of decks of 52 cards to be used in
the shoe.  The game can then be played until the shoe runs out or the user opts
out.


Dependencies
------------
	Python 3.0 or newer
	random.shuffle
	Card class from card.py
	Shoe class from shoe.py
	User and Dealer (subclasses of Player) from player.py
"""


from card import Card
from player import Dealer, Player, User
from shoe import Shoe


class Game:
	""" Initialize game of blackjack 

	Arguments
	---------
	shoe : Instance of Shoe Class
		The current shoe initialized in Blackjack.sitting()

	Parameters
	----------
	dealer : instance of Player class
	player : instance of Player class
	initial_hand_size : int
		Number of cards initially dealt
	max_target_score : int
		A constant set to 21 per the rules of blackjack
	dealer_trigger : int
		A constant set to 17, the score at which the dealer will stop accepting
		additional cards, per the rules of blackjack 
	"""
	def __init__(self, shoe):
		self.shoe = shoe
		self.dealer = Dealer(shoe)
		self.player = User(shoe)
		self.initial_hand_size = 2
		self.max_target_score = 21
		self.dealer_trigger = 17 

	def deal(self):
		""" Deals the set # of starting cards (defined in the init)"""
		player_list = [self.dealer, self.player]
		for elem in player_list:
			for x in range(self.initial_hand_size):
				if self.shoe.cards:
					elem.hand_of_cards.append(self.shoe.hand_out_card())
				else:
					return False
		return True

	def play(self):
		""" Plays a single round of blackjack 

		Returns
		-------
		winner : instance of Player object
		"""
		
		if not self.deal():
			return None
		while True:
			print("\n")
			if self.dealer.score() == 21:
				print("Dealer got a Blackjack!  You lose.")
				winner = "d"
				break
			if self.player.score() == 21:
				print("You got a Blackjack!  You win.")
				winner = "p"
				break
			
			print("Dealer has {}for a total of {}"\
				  .format(self.dealer.pretty_output(), self.dealer.score()))
			print("Player has {}for a total of {}"\
				  .format(self.player.pretty_output(), self.player.score()))
			print("\n")
			if self.dealer.interested and self.dealer.hits() and not self.dealer.get_card():
				return None
			if self.player.interested and self.player.hits() and not self.player.get_card():
				return None
			
			if self.dealer.score() > self.max_target_score:
				print("HE BUSTED!")
				print("\n")
				winner = "p"
				break
			elif self.player.score() > self.max_target_score:
				print("YOU BUSTED!")
				print("\n")
				winner = "d"
				break
			elif self.dealer.score() == 21:
				print("Dealer got a Blackjack!  You lose.")
				print("\n")
				winner = "d"
				break
			elif self.player.score() == 21:
				print("You got a Blackjack!  You win.")
				print("\n")
				winner = "p"
				break
			elif not self.dealer.interested and not self.player.interested:
				if self.player.score() <= self.dealer.score():
					winner = "d"
					print("Dealer wins.")
				else:
					winner = "p"
					print("You win.")
				break
		print("Dealer finished with: ", self.dealer.score())
		print("You had: ", self.player.score())
		print("\n")
		return winner


class Blackjack:
	""" An environment for playing blacjack.  User will define the size of the
	deck shoe (in numbers of 52 card decks) and can then play hands of
	blackjack until the shoe runs out, or they opt ou

	Attributes
	----------
	dealer_victories : int 
		Number of hands won by the dealer
	player_victories : int
		Number of hands won by the player
	"""

	def __init__(self):
		self.dealer_victories = 0
		self.player_victories = 0

	def sitting(self):
		try:
			print("\n")
			num_decks = int(input("How many decks would you like to use? "))
			assert abs(num_decks) == num_decks
		except:
			print("Sorry, we need a positive integer.")
			return
		self.shoe = Shoe(num_decks)
		self.shoe.shuffle_shoe()
		another = 'y'		# Placeholder for "Opt Out" by player
		while True:
			self.game = Game(self.shoe)
			victor = self.game.play()
			if victor == 'p':
				self.player_victories += 1
			elif victor == 'd':
				self.dealer_victories += 1
			else:
				print("Sorry, shoe is out of cards.")
				print("\n")
				break
			another = input("Would you like to play another? (y/n) ")
			if another.lower().strip() == 'n':
				break
		print("Dealer won: ", self.dealer_victories)
		print("You won: ", self.player_victories)

		
if __name__ == '__main__':
	bj = Blackjack()
	bj.sitting()
