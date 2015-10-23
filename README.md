# Blackjack
## by Cole Howard

An Implementation of the Game Blackjack
Player will be given the option to choose the size of the shoe (# of decks to use).  She will then be able to play Blackjack until the shoe runs out (or she gets tired).

Documentation: 
[![Documentation Status](https://readthedocs.org/projects/blackjack/badge/?version=latest)](http://blackjack.readthedocs.org/en/latest/?badge=latest)


Travis CI: 
[![Build Status](https://travis-ci.org/uglyboxer/Blackjack.svg?branch=master)](https://travis-ci.org/uglyboxer/Blackjack)

py.test coverage results are at the above link.

## To Get Started

Copy the folder (and its contents) Blackjack.  from inside that folder use 
the command:

```
$ python3 blackjack/bj_main.py
```
Player will be asked for a number of decks to use, then play a hand of 
blackjack.  Upon completion they will be given the option to play again,
until the shoe runs out of cards.

```
How many decks would you like to use? 1


Dealer has:
Q of Spades
3 of Clubs
For a total of 13


Player has:
2 of Spades
7 of Diamonds
For a total of 9


Would you like another card? (y/n)
```

```
Dealer won:  0
You won:  1
```

An optional merge sort method is provided via the Shoe class to return what
is left in the shoe, possibly all of it, to the order it was constructed in.
