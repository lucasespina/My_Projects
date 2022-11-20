import random
import colorama
import time



def welcome_menu():
    
    print("-"*30)
    print("\n")
    print("Welcome to Espina's Blackjack!")
    print("\n")
    print("-"*30)
    print("\nLet's play Blackjack!\n")
    print("-"*30)
    print("First I'm gonna shuffle the deck and give you two cards.\n")
    
    print("Shuffling...\n")
    
    time.sleep(1)
    
    print("Then I'm gonna give myself two cards.\n")	
    
    time.sleep(1)
    
    print("Alright, let's begin!\n")
    
def game_menu(balance, bet,dealer_hand, dealer_hand_value, player_hand, player_hand_value):
    
    print("-"*30)
    print("\nbalance: " + str(balance))
    print("bet:" + str(bet))
    print("")
    print("-"*30)

    print("\nDealer's hand is: ", dealer_hand)
    print("Dealer's hand formated is: ", dealer_hand_format(dealer_hand))
    print("Dealer's hand value is: ", dealer_hand_value)

    print("\nYour hand is: ", player_hand)
    print("Your hand value is: ", player_hand_value)
    
    


def get_hand(deck):
    hand = []
    for i in range(2):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)
    return hand

deck = [' A ♠', ' 2 ♠', ' 3 ♠', ' 4 ♠', ' 5 ♠', ' 6 ♠', ' 7 ♠', ' 8 ♠', ' 9 ♠', ' 10 ♠', ' J ♠', ' Q ♠', ' K ♠', ' A ♣', ' 2 ♣', ' 3 ♣', ' 4 ♣', ' 5 ♣', ' 6 ♣', ' 7 ♣', ' 8 ♣', ' 9 ♣', ' 10 ♣', ' J ♣', ' Q ♣', ' K ♣', ' A ♥', ' 2 ♥', ' 3 ♥', ' 4 ♥', ' 5 ♥', ' 6 ♥', ' 7 ♥', ' 8 ♥', ' 9 ♥', ' 10 ♥', ' J ♥', ' Q ♥', ' K ♥', ' A ♦', ' 2 ♦', ' 3 ♦', ' 4 ♦', ' 5 ♦', ' 6 ♦', ' 7 ♦', ' 8 ♦', ' 9 ♦', ' 10 ♦', ' J ♦', ' Q ♦', ' K ♦']


def get_value(hand):
    
    value = 0
    for card in hand:
        if card[1] == 'A':
            value += 11
        elif card[1] in ['J', 'Q', 'K']:
            value += 10
        else:
            
            return value    
        

def dealer_hand_format(dealer_hand):
    dealer_hand[1] = "X"
    dealer_hand = "  ".join(dealer_hand)
    return dealer_hand


player_hand = get_hand(deck)
player_hand_value = get_value(player_hand)

print(player_hand,player_hand_value)