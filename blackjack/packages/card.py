class Card:
    """ Class of a single card in a traditional deck of 52 cards.
    Cards are 2 - 10 and have a value matching their integer name.
    or the are a 'face' card (Jack, Queen, King) and valued at 10.
    Ace cards are valued at 1 or 11 depending on the state of the rest of the
        hand.

    Parameters
    ----------
    input_card : tuple
      A 3-value tuple composed of:
        card_name : string
            The name of the card from the traditional set of playing cards.
        suit : string
            One of ('H', 'D', 'C', 'S') representing the four possible suits.
        orig_loc : int
            The card's original location in the shoe at "construction" time

    Attributes
    ----------
    card_name : string
        The "rank" of given card instance
    suit : string
        The "suit"
    orig_loc : int
        The integer representing the location in the original shoe, before any
        shuffling
    value : int
        The integer value (from 1 - 11) of a card's worth in the game of
        Blackjack.
        
    """

    def __init__(self, input_card):
        self.card_name = input_card[0]
        self.suit = input_card[1]
        self.orig_loc = input_card[2]
        self.value = self.assign_value()

    def assign_value(self):
        val_dict = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                    '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        return val_dict[self.card_name]

    def flip_ace(self):
        """ For imposing a new vaule if the status of the game requires it. """
        if self.card_name != 'A':
            return "Not an ace!"
        elif self.value == 1:
            self.value = 11
        else:
            self.value = 1

if __name__ == '__main__':
    main()
