# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:11:02 2019

@author: Jatin
"""

from BlackJAck import BlackJack

class PlayBlackJAck:     
        
    playGame = BlackJack()
    while(playGame.gameOverFlag == False):
        print("*"*10,"Classic BlackJack Game","*"*10)
        print("\n Game Menu :\n 1.(P)lay Game\n 2.(Q)uit")
        print("*"*45)
        choice = input("Press P to play & Q to quit >>> ").lower().rstrip()
        print("\n"+"*"*45)
        if choice=="q":
            break
        
        elif choice=="p":
            cardsDeck = playGame.createDeck()
            userList = playGame.userDrawnCards(playGame.drawSingleCard())
            print("User Hand :",playGame.totalHand(userList))
            print("*"*45)
            computerList = playGame.computerDrawnCards(playGame.drawSingleCard())
            print("Computer Hand: ",playGame.totalHand(computerList))
            print("*"*45)
            userList = playGame.userDrawnCards(playGame.drawSingleCard())
            print("User Hand :",playGame.totalHand(userList))
            print("*"*45)
            playGame.calculateWinner(userList,computerList)
            
        else:
            print("\nInvalid choice, please choose again\n")

    print("Thank you for playing,")
        
    