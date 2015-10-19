import nose

from blackjack.blackjack import Card


class TestCardClass(unittest.TestCase):

	def setUp(self):
		self.card = Card('K')

	def test_assign_value(self):
		self.assertEqual(self.card.value, 10)

	def tearDown(self):
		self.card.dispose()

if __name__ == '__main__':
	unittest.main()