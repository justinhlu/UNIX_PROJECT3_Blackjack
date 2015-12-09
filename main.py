# File: main.py
# Modified: 12/11/15
# Authors: Justin Lu and Richard Ma
# Description: Main file for blackjack game
# http://stackoverflow.com/questions/2518753/best-way-to-implement-a-deck-for-a-card-game-in-python
import random
import sys
import os
import itertools
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
for index in range(len(hand_dealer)):
    if(hand_dealer[index]=='T'):
        dealerValue+=10
    elif(hand_dealer[index]=='J'):
        dealerValue+=10
    elif(hand_dealer[index]=='K'):
        dealerValue+=10
    elif(hand_dealer[index]=='Q'):
        dealerValue+=10
    elif(hand_dealer[index]=='A'):
        dealerValue+=1
    else:
        dealerValue += int(hand_dealer[index])
print dealerValue


#need to remove cards from deck to ensure no duplicates if we're playing multiple rounds


#Functions for player actions

def deal():
    pass

def hit(hand):
    #add a new card to the hand
    newCard = random.sample(DECK, 1)
    hand.append(newCard)
    print hand

def bust (player):
    print 'Bust!'
    print player + 'loses!'

def stand():
    pass

def newBlackjackGame():
    pass