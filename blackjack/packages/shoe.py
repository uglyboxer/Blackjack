from random import shuffle

from .card import Card


class Shoe():

    """ A shoe of cards made out of a number of traditional decks.  User will
    be asked for the number of decks to put in the shoe.

    Parameters
    ----------
    num_decks : int
        The number of decks supplied by the user.
        Defaults to 1 deck.

    Attributes
    ----------
    num_decks : int
        Number of 52 card decks to use
    cards : list
        List of instances of card object returned by the constructor method

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

        Attributes
        ----------
        cards : list
            A list of the cards currently available to the players
        suits : list
            A list of strings reprsenting the 4 suits possible in a deck

        Returns
        -------
        list
            A list of cards that is a (num_decks) multiple of standard
            52 card decks.

        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        possible_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J',
                          'Q', 'K', 'A']

        #  Third element of tuple in the list is a formula for getting
        #  0 - 155, or whatever for flattening the index of a 3d array
        #  (decks * ((13 * x) + y)) + z
        return [Card((c, elem, (self.num_decks)*(((len(possible_cards) * idx) +
                idy) + i))) for idx, elem in enumerate(suits)
                            for idy, c in enumerate(possible_cards)
                            for i in range(self.num_decks)]

    def shuffle_shoe(self):
        """ Shuffles the order of the cards in the list that constitues the
        shoe.

        Returns
        -------
        True
            For evidence of exectution

        """
        shuffle(self.cards)
        return True

    def hand_out_card(self):
        """ Takes the top card, aka the last card in the list of cards and
        removes it from the list and returns it.

        Returns
        -------
        bool
            Based on success of execution.

        """
        if self.cards:
            return self.cards.pop()
        else:
            return False

    def cards_left(self):
        """ Not currently accessed by any part of the script, other than the
        testing suite.

        Returns
        -------
        int
            The length of list that is self.cards

        """
        return len(self.cards)

    def merge_sort(self, lst):
        """ Not currently accessed by any part of the script, other than the
        testing suite.

        Parameters
        ----------
        lst : list
            A list of "orderable" objects.

        Returns
        -------
        list
            A new list of the same elements - sorted.

        """
        if len(lst) <= 1:  # Empty list or just 1 item.
            return lst
        else:
            mid = len(lst)//2
            left = self.merge_sort(lst[:mid])
            right = self.merge_sort(lst[mid:])
            temp_lst = []
            while left and right:
                if left[0].orig_loc > right[0].orig_loc:
                    temp_lst.append(right.pop(0))
                else:
                    temp_lst.append(left.pop(0))
            if left:
                temp_lst += left
            else:
                temp_lst += right
        return temp_lst
