# File: main.py
# Modified: 12/11/15
# Authors: Justin Lu and Richard Ma
# Description: Main file for blackjack game
#http://stackoverflow.com/questions/2518753/best-way-to-implement-a-deck-for-a-card-game-in-python
import random
import itertools
SUITS = 'cdhs'
RANKS = '23456789TJQKA'
DECK = tuple(''.join(card) for card in itertools.product(RANKS, SUITS))
hand = random.sample(DECK, 5)
print hand
print hand.pop()
