import unittest

from blackjack.bj_main import Game
from blackjack.packages.card import Card
from blackjack.packages.shoe import Shoe
from blackjack.packages.player import Dealer, Player, User


class TestCardClass(unittest.TestCase):

    def test_assign_value(self):
        self.card = Card(('K', 'S', 1))
        self.assertEqual(self.card.value, 10)

    def test_flip_value(self):
        self.card = Card(('A', 'H', 1))
        self.assertEqual(self.card.value, 11)
        self.card.flip_ace()
        self.assertEqual(self.card.value, 1)
        self.card.flip_ace()
        self.assertEqual(self.card.value, 11)

    def test_bad_ace(self):
        self.card = Card(('3', 'C', 1))
        self.assertEqual(self.card.flip_ace(), "Not an ace!")


class TestShoeClass(unittest.TestCase):

    def test_constructor(self):
        self.shoe = Shoe(1)

        self.assertEqual(len(self.shoe.cards), 52)

    def test_merge_sort(self):
        self.shoe1 = Shoe(1)
        original_shoe = self.shoe1.cards[:]
        self.shoe1.shuffle_shoe()
        self.assertNotEqual(self.shoe1.cards, original_shoe)
        sorted_shoe = self.shoe1.merge_sort(self.shoe1.cards)
        self.assertEqual(sorted_shoe, original_shoe)

    def test_cards_left(self):
        self.shoe = Shoe(1)
        self.assertEqual(self.shoe.cards_left(), 52)
        self.shoe.hand_out_card()
        self.assertEqual(self.shoe.cards_left(), 51)
        self.shoe1 = Shoe(3)
        self.assertEqual(self.shoe1.cards_left(), 156)


class TestPlayerClass(unittest.TestCase):

    def test_score_aces(self):
        self.shoe = Shoe(1)
        self.hand = Player(self.shoe)
        self.card1 = Card(('A', 'S', 1))
        self.card2 = Card(('A', 'H', 2))
        self.hand.hand_of_cards.append(self.card1)
        self.hand.hand_of_cards.append(self.card2)
        self.assertEqual(self.hand.score(), 12)

    def test_score_(self):
        self.shoe = Shoe(1)
        self.hand = Dealer(self.shoe)
        self.card1 = Card(('K', 'S', 1))
        self.card2 = Card(('3', 'H', 2))
        self.hand.hand_of_cards.append(self.card1)
        self.hand.hand_of_cards.append(self.card2)
        self.assertEqual(self.hand.score(), 13)

    def test_get_card(self):
        self.shoe = Shoe(1)
        self.hand = Dealer(self.shoe)
        self.assertEqual(self.hand.get_card(), True)
        self.assertEqual(len(self.hand.hand_of_cards), 1)
        self.assertEqual(self.hand.hits(), True)

    def test_pretty_output(self):
        self.shoe = Shoe(1)
        self.hand = Dealer(self.shoe)
        self.card1 = Card(('K', 'S', 1))
        self.card2 = Card(('K', 'H', 2))
        self.hand.hand_of_cards.append(self.card1)
        self.hand.hand_of_cards.append(self.card2)
        self.assertEqual(self.hand.pretty_output(), 'K K ')


class TestGameClass(unittest.TestCase):

    def test_game(self):
        self.shoe = Shoe(1)
        self.shoe.shuffle_shoe()
        self.game = Game(self.shoe)
        self.game.deal()
        self.assertEqual(len(self.game.dealer.hand_of_cards), 2)
        self.assertEqual(len(self.game.player.hand_of_cards), 2)


class TestDealerClass(unittest.TestCase):

    def test_hits(self):
        self.shoe = Shoe(1)
        self.hand = Dealer(self.shoe)
        self.card1 = Card(('K', 'S', 1))
        self.card2 = Card(('K', 'H', 2))
        self.hand.hand_of_cards.append(self.card1)
        self.hand.hand_of_cards.append(self.card2)
        self.assertEqual(self.hand.hits(), False)


if __name__ == '__main__':
    unittest.main()
