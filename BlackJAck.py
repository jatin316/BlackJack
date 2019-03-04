# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 19:40:11 2019

@author: Jatin
"""

import random as r


class BlackJack:
    def __init__(self):
        self.userHand = []
        self.computerHand = []
        self.cardsDeck = []
        self.aceValue = 0
        self.hitFlag = True
        self.gameOverFlag = False
# =============================================================================
#   @createDeck(self)
#   @Desciption: Creates a list of Dictionaries which contains a pair of 
#                suit and card face value
#   @Returns : A List of Dictinary
# =============================================================================
    def createDeck(self):
        cards = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.cardsDeck= [{'value':i,'suit':c} for c in ['spades','clubs','hearts','diamonds'] for i in cards]
        return self.cardsDeck

# =============================================================================
#   @drawSingleCard(self)
#   @Desciption: This method first randomly shuffles the list of cards 
#                then rmoves a card from the last by using pop function
#                
#   @Function:Random.shuffle,List.pop    
#   @Returns : a card in form of dictinory(key:value) 
# =============================================================================
                
    def drawSingleCard(self):
        print("Dealer Shuffeling the Cards Deck.....!") 
        r.shuffle(self.cardsDeck)
        drawnCard = self.cardsDeck.pop()
        return drawnCard    
# =============================================================================
#   @userDrawnCards(self,card)
#   @Desciption: This method stores the cards drawn by the user from the deck
#                into a list of type dictinory
#                
#   @Parameter:card(Dictinory)
#   @Function:List.append    
#   @Returns : A list of dictinory 
# =============================================================================       
    def userDrawnCards(self,card):
        print("User Drawn :",card)
        self.userHand.append(card)
        return self.userHand
# =============================================================================
#   @computerDrawnCards(self,card)
#   @Desciption: This method stores the cards drawn by the computer from the deck
#                into a list of type dictinory
#                
#   @Parameter:card(Dictinory)
#   @Function:List.append    
#   @Returns : A list of dictinory 
# =============================================================================   
    def computerDrawnCards(self,card):
        print("Computer Draws :",card)
        self.computerHand.append(card)
        return self.computerHand
# =============================================================================
#   @totalHand(self,handList)
#   @Desciption: This method calculates the sum of card values.
#                
#   
#   @Parameter:handList(List of dictionary)
#      
#   @Returns : currentHandTotal 
# =============================================================================     
    def totalHand(self,handList):
        currentHandTotal = 0
        for card in handList:
            if('Ace' in card['value']):
                if(currentHandTotal < 10):
                    print("Ace value is considered as 11")
                    card['value'] = '11'
                    currentHandTotal +=int(card['value'])
                else:
                    print("Ace value is considered as 1")
                    card['value'] = '1'
                    currentHandTotal +=int(card['value'])
                    
            elif(card['value'] in ['Jack','Queen','King']):
                currentHandTotal += 10
            else:
                currentHandTotal += int(card['value'])
        return currentHandTotal
# =============================================================================
#   @calculateWinner(self,userList,computerList)
#        
#   @Desciption: This method calculates sum of hands for user and dealer and
#               based on the handTotal decides the furthur game play 
#                
#   
#   @Parameter:userList,computerList
#      
#
# =============================================================================
    def calculateWinner(self,userList,computerList):
        userScore = self.totalHand(userList)
        computerScore = self.totalHand(computerList) 
        if( userScore > 21 ):
            print("Player Busted !!!, Dealer Wins!!")
            self.gameOverFlag = True
        elif(computerScore > 21):
            print("Computer Busted !!!, Player Wins ")
            self.gameOverFlag = True
        elif(userScore < 21 and self.hitFlag == True):
            print("*"*45)
            print("\nPlayer Options: \n1.Hit \n2.Stand")
            option = int(input("Select an Option to play further:"))
            print("*"*45)
            if(option == 1):
                self.userDrawnCards(self.drawSingleCard())
                print("User Hand :",self.totalHand(self.userHand))
                self.calculateWinner(self.userHand,self.computerHand)
                print("*"*45)
            elif(option == 2):
                self.hitFlag = False
                self.computerDrawnCards(self.drawSingleCard())
                print("Computer Hand :",self.totalHand(self.computerHand))
                self.calculateWinner(self.userHand,self.computerHand)
                print("*"*45)
                
        elif(computerScore < 17):
            print("Dealer shows his cards....!!")
            self.computerDrawnCards(self.drawSingleCard())
            print("Computer Hand :",self.totalHand(self.computerHand))
            self.calculateWinner(self.userHand,self.computerHand)
            print("*"*45)
        elif(userScore < 21 and computerScore < 21 ):
            if(userScore < computerScore):
                print("*"*45)
                print("Dealer Wins ....!!!")
                self.gameOverFlag = True
            elif(computerScore < userScore):
                print("*"*45)
                print("user wins .....!!!")
                self.gameOverFlag = True
        elif(userScore == computerScore):
            print("*"*45)
            print("Equal Deals, no winner.....Its a PUSH!!")
            self.gameOverFlag = True
        