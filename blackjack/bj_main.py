""" blackjack.py
Author: Cole Howard

A simple implementation of the game of blackjack.

The user is tasked with defining the number of decks of 52 cards to be used in
the shoe.  The game can then be played until the shoe runs out or the user opts
out.   Dealer always wins ties.

Usage
-----

Copy the folder Blackjack (capital B) and run the script:

>>>python3 blackjack/bj_main.py

All interaction will be via stdout on the command line.

Tests can be run from the same directory via

>>>nosetests

or

>>>py.test

Dependencies:
    Python 3.0 or newer
    random.shuffle
    Card class from card.py
    Shoe class from shoe.py
    User and Dealer (subclasses of Player) from player.py


"""


from blackjack.packages.card import Card
from blackjack.packages.player import Dealer, Player, User
from blackjack.packages.shoe import Shoe


class Game:
    """ Initialize game of blackjack

    Parameters
    ---------
    shoe : Instance of Shoe Class
        The current shoe initialized in Blackjack.sitting()


    Attributes
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

    def report(self, finished=False):
        """ Reports the status of the game to the stdout on command line """
        
        if finished is False:
            verb = "has"
        else:
            verb = "had"
        print(chr(27) + "[2J")
        print("Dealer {}: {}For a total of {}"
              .format(verb, self.dealer.pretty_output(), self.dealer.score()))
        print("\n")
        print("Player {}: {}For a total of {}"
              .format(verb, self.player.pretty_output(), self.player.score()))
        print("\n")

    def eval_state(self):
        """ Evaluates the status of the game to the stdout on command line

        Returns
        -------
        string
            "d", "p", or None (if out of cards or unresolved)
        """
        winner = None
        if self.dealer.status["bj"] or self.player.status["bust"]:
            winner = "d"
        elif self.player.status["bj"] or self.dealer.status["bust"]:
            winner = "p"
        return winner

    def get_winner(self):
        """ Determines the winner if both players pass

        Returns
        -------
        string 
            "d" (dealer) or "p" (player) for victor

        """
        if self.player.score() <= self.dealer.score():
            return "d"
        else:
            return "p"


    def report_results(self):
        """ Report final outcome of the hand

        Returns
        -------
        True
            As notification of execution

        """
        print("Dealer finished with: ", self.dealer.score())
        print("You had: ", self.player.score())
        print("\n")
        return True

    def play(self):
        """ Plays a single round of blackjack

        Returns
        -------
        instance of Player object
        
        """

        if not self.deal():
            return None  # .hand_out_card reports back no more cards
        if not self.dealer.update_status() or\
               not self.player.update_status():
                print("Something went wrong.")
        winner = self.eval_state()        
        while not winner:
            self.report()
            if self.dealer.status["interested"] and self.dealer.hits() and\
               not self.dealer.get_card():
                return None  # .get_card reports back no more cards
            elif self.player.status["interested"] and self.player.hits() and\
                 not self.player.get_card():
                return None  # .get_card reports back no more cards
            
            if not self.dealer.update_status() or\
               not self.player.update_status():
                print("Something went wrong.")  # If update fails 
            winner = self.eval_state()
            if winner:
                break
            elif not self.dealer.status["interested"] and\
                 not self.player.status["interested"]:
                winner = self.get_winner()
                break
        self.report(finished=True)
        if self.report_results():
            
            return winner 
        else:
            print("Something went wrong.")
            return None


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
            print("\n")
            assert abs(num_decks) == num_decks
        except:
            print("Sorry, we need a positive integer.")
            return
        self.shoe = Shoe(num_decks)
        self.shoe.shuffle_shoe()
        another = 'y'       # Placeholder for "Opt Out" by player
        while True:
            self.game = Game(self.shoe)
            victor = self.game.play()
            if victor == 'p':
                print("You win!")
                print("\n")
                self.player_victories += 1
            elif victor == 'd':
                print("Dealer won.")
                print("\n")
                self.dealer_victories += 1
            else:
                print("Sorry, shoe is out of cards.")
                print("\n")
                break
            another = input("Would you like to play another? (y/n) ")
            print(chr(27) + "[2J")
            if another.lower().strip() == 'n':
                break
        print("\n")
        print("Dealer won: ", self.dealer_victories)
        print("You won: ", self.player_victories)
        print("\n")


if __name__ == '__main__':
    bj = Blackjack()
    bj.sitting()
