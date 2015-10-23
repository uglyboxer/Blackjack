class Player:
    """ The hand of cards for a given player

    Parameters
    ---------
    shoe : Instance of Shoe Class
        The current shoe initialized in Blackjack.sitting()

    Attributes
    ----------
    hand_of_cards : list
        A list of cards in the current hand.
    max_target_score : int
        A constant set to 21 per the rules of blackjack
    status : dict
        A dictionary of bools, representing:
           "bj" : Score a Blackjack?
           "bust" : Bust(go over 21) yet?
           "interested" : Interested in receiving another card when offereds

    """

    def __init__(self, shoe):
        self.shoe = shoe
        self.hand_of_cards = []
        self.max_target_score = 21
        self.status = {"bj": False, "bust": False, "interested": True}

    def score(self):
        """ Calculates the current score of the hand """

        total = sum([card.value for card in self.hand_of_cards])
        if total > self.max_target_score:
            for card in self.hand_of_cards:
                if card.value == 11:  # The value of an ace, can be flipped to 1
                    card.flip_ace()
                    total = sum([card.value for card in
                                 self.hand_of_cards])
                    break   # So only one ace gets flipped.
        return total

    def pretty_output(self):
        """ Creates a string of the current cards for output """
        full_hand = ""
        for card in self.hand_of_cards:
            full_hand += "\n" + card.card_name + " of " + card.suit
        return full_hand + "\n"

    def get_card(self):
        """ Gets a new card from the shoe """
        if self.shoe.cards:
            self.hand_of_cards.append(self.shoe.hand_out_card())
            return True
        else:
            return False

    def update_status(self):
        """ Updates a players status based on score of current hand_of_cards

        Returns
        -------
        True
          As evidence of executing

        """
        if self.score() == self.max_target_score:
            self.status["bj"] = True
        elif self.score() > self.max_target_score:
            self.status["bust"] = True
        return True


class Dealer(Player):
    """ A subclass of the class Player, with a method to determine if he hits
    or not in a given situation.

    """

    def hits(self):
        dealer_stays_on = 17
        if self.score() < dealer_stays_on:
            return True
        else:
            self.status["interested"] = False
            return False


class User(Player):
    """ A subclass of the class Player, with a method to determine if he hits
    or not in a given situation.

    """

    def hits(self):
        while True:
            choice = input("Would you like another card? (y/n) ")
            print("\n")
            if choice.lower().strip() == 'y':
                return True
            elif choice.lower().strip() == 'n':
                self.status["interested"] = False
                return False
            else:
                print("y or n are the only valid responses.")
