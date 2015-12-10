# File: main.py
# Modified: 12/11/15
# Authors: Justin Lu and Richard Ma
# Description: Main file for blackjack game
# http://stackoverflow.com/questions/2518753/best-way-to-implement-a-deck-for-a-card-game-in-python
# Rules of Blackjack found at:
# http://www.pagat.com/banking/blackjack.html#player
import random
import sys
import os
import itertools
PlayerMoney = 1000
RANKS = '23456789TJQKA'
DECK = tuple(''.join(card) for card in itertools.product(RANKS))

#need to remove cards from deck to ensure no duplicates if we're playing multiple rounds


#Functions for player actions


def hit(hand):
    #add a new card to the hand
    newCard = random.sample(DECK, 1)
    hand.append(newCard[0])
    print hand

def bust (player):
    #if player hand value is over 21, they lose
    print 'Bust!'
    print player + ' loses!'


def getHandValue(hand):
    value = 0
    for index in range(len(hand)):
        if(hand[index]=='T'):
            value+=10
        elif(hand[index]=='J'):
            value+=10
        elif(hand[index]=='K'):
            value+=10
        elif(hand[index]=='Q'):
            value+=10
        elif(hand[index]=='A'):
            value+=1
        else:
            value += int(hand[index])
    if('A' in hand and value<=11):
            value+=10

    return value

def stand():
    pass

def newBlackjackGame():
    continuePlaying = True

    dealerValue=0
    playerValue=0
    gamesWon = 0


    # PLAYER'S TURN
    while (continuePlaying == True):
        global PlayerMoney
        print 'You have ${0:0.2f}'.format(PlayerMoney)
        bet = raw_input ('PLAYERS TURN: How much money do you want to bet? ')
        while(int(bet)>PlayerMoney):
            print "Can't bet that much"
            bet = raw_input ('PLAYERS TURN: How much money do you want to bet? ')



        isPlayerBust = False
        isHouseBust = False
        playerTurnOver = False
        dealerTurnOver = False
        hand_player = random.sample(DECK, 2)
        hand_dealer = random.sample(DECK, 2)
        print "Player"
        print (hand_player)
        playerValue = getHandValue(hand_player)
        print playerValue

        print "Dealer"
        print (hand_dealer[1])
        dealerValue = getHandValue(hand_dealer)
        while (playerTurnOver == False):
            action = raw_input ('PLAYERS TURN: Would you like to hit or stand? Type "hit", "stand", "help." ')
            if (action == 'help'):
                print 'T = 10, J = 10, Q = 10, K = 10, A can be 1 or 11'
            elif (action == 'hit'):
                hit (hand_player)
                playerValue = getHandValue(hand_player)
                print playerValue
                if (playerValue > 21):
                    isPlayerBust = True
                    bust ('Player')
                    break
            elif (action == 'stand'):
                playerTurnOver = True
            else:
                print 'INVALID ACTION'
    # DEALER'S TURN
        while (dealerTurnOver == False and isPlayerBust != True):
            dealerValue = getHandValue (hand_dealer)
            if (dealerValue < 17): # dealer must hit if hand value is lower than 17
                hit(hand_dealer)
                dealerValue = getHandValue(hand_dealer)
                if (dealerValue > 21):
                    isHouseBust = True
                    bust('Dealer')
                    break
                else:
                    dealerTurnOver = True
            elif (dealerValue == 21): # dealer has blackjack
                dealerTurnOver = True
            else:
                dealerTurnOver = True

        dealerValue = getHandValue(hand_dealer)
        playerValue = getHandValue(hand_player)

        print 'Value of Player Hand: ' + str(playerValue)
        print 'Value of Dealer Hand: ' + str(dealerValue)

        if (playerValue > dealerValue and isPlayerBust == False):
            print 'Player wins!'
            gamesWon+=1
            print 'Games won by Player: ' + str(gamesWon)
            PlayerMoney += int(bet)
            print 'You have ${0:0.2f}'.format(PlayerMoney)
        elif (isHouseBust == True):
            print 'Player wins!'
            gamesWon+=1
            print 'Games won by Player: ' + str(gamesWon)
            PlayerMoney += int(bet)
            print 'You have ${0:0.2f}'.format(PlayerMoney)
        else:
            print 'House wins!'
            PlayerMoney -= int(bet)
            print 'You have ${0:0.2f}'.format(PlayerMoney)

        if(PlayerMoney<=0):
            print 'Out of Money!'
            continuePlaying = False
            break
        else:
            cont = raw_input('Would you like to continue playing? Type "No" to walk away or "Yes" to continue')
            if (cont == 'No' or cont == ' No' or cont == 'no'):
                continuePlaying = False
                break
newBlackjackGame()
#test committ 7:35