import unittest

# import blackjack.bj_main
from blackjack.bj_main import Game
from blackjack.packages.card import Card
from blackjack.packages.shoe import Shoe
from blackjack.packages.player import Dealer, Player, User


class TestCardClass(unittest.TestCase):

	def test_assign_value(self):
		self.card = Card(('K', 'S'))
		self.assertEqual(self.card.value, 10)

	def test_flip_value(self):
		self.card = Card(('A', 'H'))
		self.assertEqual(self.card.value, 11)
		self.card.flip_ace()
		self.assertEqual(self.card.value, 1)
		self.card.flip_ace()
		self.assertEqual(self.card.value, 11)

	def test_bad_ace(self):
		self.card = Card(('3', 'C'))
		self.assertEqual(self.card.flip_ace(), "Not an ace!")

class TestShoeClass(unittest.TestCase):

	def test_constructor(self):
		self.shoe = Shoe(1)
		self.assertEqual(len(self.shoe.cards), 52)

	def test_merge_sort(self):
		self.FIXME

class TestPlayerClass(unittest.TestCase):

	def test_score_aces(self):
		self.shoe = Shoe(1)
		self.hand = Player(self.shoe)
		self.card1 = Card(('A', 'S'))
		self.card2 = Card(('A', 'H'))
		self.hand.hand_of_cards.append(self.card1)
		self.hand.hand_of_cards.append(self.card2)
		self.assertEqual(self.hand.score(), 12)

	def test_score_(self):
		self.shoe = Shoe(1)
		self.hand = Dealer(self.shoe)
		self.card1 = Card(('K', 'S'))
		self.card2 = Card(('3', 'H'))
		self.hand.hand_of_cards.append(self.card1)
		self.hand.hand_of_cards.append(self.card2)
		self.assertEqual(self.hand.score(), 13)  

class TestGameClass(unittest.TestCase):

	def test_game(self):
		self.shoe = Shoe(1)
		self.shoe.shuffle_shoe()
		self.game = Game(self.shoe)
		self.game.deal()
		self.assertEqual(len(self.game.dealer.hand_of_cards), 2)
		self.assertEqual(len(self.game.player.hand_of_cards), 2)


if __name__ == '__main__':
	unittest.main()