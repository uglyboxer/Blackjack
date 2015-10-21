# Blackjack
## by Cole Howard

An Implementation of the Game Blackjack
Player will be given the option to choose the size of the shoe (# of decks to use).  She will then be able to play Blackjack until the shoe runs out (or she gets tired).

Documentation lives [here](http://wwww.readthedocs.org)

TravisCI button will live here.

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


Dealer has 7 5 for a total of 12
Player has Q 2 for a total of 12


Would you like another card? (y/n) y


HE BUSTED!


Dealer finished with:  22
You had:  21


Would you like to play another? (y/n) n
Dealer won:  0
You won:  1
```

An optional merge sort method is provided via the Shoe class to return what
is left in the shoe, possibly all of it, to the order it was constructed in.