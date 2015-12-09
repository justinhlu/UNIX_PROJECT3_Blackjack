# File: main.py
# Modified: 12/11/15
# Authors: Justin Lu and Richard Ma
# Description: Main file for blackjack game
# http://stackoverflow.com/questions/2518753/best-way-to-implement-a-deck-for-a-card-game-in-python
import random
import sys
import os
import itertools
#SUITS = 'cdhs'
RANKS = '23456789TJQKA'
DECK = tuple(''.join(card) for card in itertools.product(RANKS))

hand_player = random.sample(DECK, 2)
hand_dealer = random.sample(DECK, 2)
print "Player"
print (hand_player)
hand_player.append(random.sample(DECK, 1)[0])
print (hand_player)

print "Dealer"
print (hand_dealer)
print (hand_dealer[1])
dealerValue=0



#need to remove cards from deck to ensure no duplicates if we're playing multiple rounds

#define Hand class
class Hand:
    def __init__(self):
        pass #pass statement indicates code needs to go here
    def __str__(self):
        pass
    def add(self):
        pass
    def getVal(self):
        pass

class Deck:
    def __init__(self):
        pass
    def __str__(self):
        pass
    def deal(self):
        pass
    def shuffle(self):
        pass
#Functions for player actions

def deal():
    pass

def hit():
    pass

def stand():
    pass

def draw():
    pass
