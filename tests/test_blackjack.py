import unittest

from blackjack.bj_main import Blackjack, Game
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
        self.card1 = Card(('K', 'Spades', 1))
        self.card2 = Card(('K', 'Hearts', 2))
        self.hand.hand_of_cards.append(self.card1)
        self.hand.hand_of_cards.append(self.card2)
        self.assertEqual(self.hand.pretty_output(), '\nK of Spades\nK of Hearts\n')

    def test_update_status(self):
        self.shoe = Shoe(1)
        self.hand = Dealer(self.shoe)
        self.card1 = Card(('K', 'S', 1))
        self.card2 = Card(('6', 'H', 2))
        self.card3 = Card(('8', 'H', 3))
        self.hand.hand_of_cards.append(self.card1)
        self.hand.hand_of_cards.append(self.card2)
        self.hand.update_status()
        self.assertEqual(self.hand.status["bj"], False)
        self.assertEqual(self.hand.status["interested"], True)
        self.assertEqual(self.hand.status["bust"], False)
        self.hand.hand_of_cards.append(self.card3)
        self.hand.hits()
        self.hand.update_status()
        self.assertEqual(self.hand.status["bj"], False)
        self.assertEqual(self.hand.status["interested"], False)
        self.assertEqual(self.hand.status["bust"], True)



class TestGameClass(unittest.TestCase):

    def test_game(self):
        self.shoe = Shoe(1)
        self.shoe.shuffle_shoe()
        self.game = Game(self.shoe)
        self.game.deal()
        self.assertEqual(len(self.game.dealer.hand_of_cards), 2)
        self.assertEqual(len(self.game.player.hand_of_cards), 2)

    def test_eval_state(self):
        self.shoe = Shoe(1)
        self.game = Game(self.shoe)
        self.card1 = Card(('2', 'S', 1))
        self.card2 = Card(('7', 'H', 2))
        self.card3 = Card(('K', 'S', 1))
        self.card4 = Card(('A', 'H', 2))
        self.game.player.hand_of_cards.append(self.card1)
        self.game.player.hand_of_cards.append(self.card2)
        self.game.dealer.hand_of_cards.append(self.card3)
        self.game.dealer.hand_of_cards.append(self.card4)
        self.game.dealer.update_status()
        self.game.player.update_status()
        self.assertEqual(self.game.eval_state(), "d")

        self.shoe = Shoe(1)
        self.game = Game(self.shoe)
        self.card1 = Card(('K', 'S', 1))
        self.card2 = Card(('A', 'H', 2))
        self.card3 = Card(('7', 'S', 1))
        self.card4 = Card(('10', 'H', 2))
        self.game.player.hand_of_cards.append(self.card1)
        self.game.player.hand_of_cards.append(self.card2)
        self.game.dealer.hand_of_cards.append(self.card3)
        self.game.dealer.hand_of_cards.append(self.card4)
        self.game.dealer.update_status()
        self.game.player.update_status()
        self.assertEqual(self.game.eval_state(), "p")

    def test_get_winner(self): 
        self.shoe = Shoe(1)
        self.game = Game(self.shoe)
        self.card1 = Card(('10', 'S', 1))
        self.card2 = Card(('7', 'H', 2))
        self.card3 = Card(('K', 'S', 1))
        self.card4 = Card(('9', 'H', 2))
        self.game.player.hand_of_cards.append(self.card1)
        self.game.player.hand_of_cards.append(self.card2)
        self.game.dealer.hand_of_cards.append(self.card3)
        self.game.dealer.hand_of_cards.append(self.card4)
        self.game.dealer.update_status()
        self.game.player.update_status()
        self.assertEqual(self.game.get_winner(), "d")

        self.shoe = Shoe(1)
        self.game = Game(self.shoe)
        self.card1 = Card(('9', 'S', 1))
        self.card2 = Card(('A', 'H', 2))
        self.card3 = Card(('K', 'S', 1))
        self.card4 = Card(('9', 'H', 2))
        self.game.player.hand_of_cards.append(self.card1)
        self.game.player.hand_of_cards.append(self.card2)
        self.game.dealer.hand_of_cards.append(self.card3)
        self.game.dealer.hand_of_cards.append(self.card4)
        self.game.dealer.update_status()
        self.game.player.update_status()
        self.assertEqual(self.game.get_winner(), "p")     

class TestDealerClass(unittest.TestCase):

    def test_hits(self):
        self.shoe = Shoe(1)
        self.hand = Dealer(self.shoe)
        self.card1 = Card(('K', 'S', 1))
        self.card2 = Card(('K', 'H', 2))
        self.hand.hand_of_cards.append(self.card1)
        self.hand.hand_of_cards.append(self.card2)
        self.assertEqual(self.hand.hits(), False)

class TestBlackjackClass(unittest.TestCase):

    def test__init__(self):
        self.bj = Blackjack()
        self.bj.dealer_victories == 0
        self.bj.player_victories == 0

if __name__ == '__main__':
    unittest.main()
