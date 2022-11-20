import random
import colorama
from assets import functions

colors = ["black", "red"]

deck = [' A ♠', ' 2 ♠', ' 3 ♠', ' 4 ♠', ' 5 ♠', ' 6 ♠', ' 7 ♠', ' 8 ♠', ' 9 ♠', ' 10 ♠', ' J ♠', ' Q ♠', ' K ♠', ' A ♣', ' 2 ♣', ' 3 ♣', ' 4 ♣', ' 5 ♣', ' 6 ♣', ' 7 ♣', ' 8 ♣', ' 9 ♣', ' 10 ♣', ' J ♣', ' Q ♣', ' K ♣', ' A ♥', ' 2 ♥', ' 3 ♥', ' 4 ♥', ' 5 ♥', ' 6 ♥', ' 7 ♥', ' 8 ♥', ' 9 ♥', ' 10 ♥', ' J ♥', ' Q ♥', ' K ♥', ' A ♦', ' 2 ♦', ' 3 ♦', ' 4 ♦', ' 5 ♦', ' 6 ♦', ' 7 ♦', ' 8 ♦', ' 9 ♦', ' 10 ♦', ' J ♦', ' Q ♦', ' K ♦']


functions.welcome_menu()

balance = float(input("How much money do you want to start with ? "))


while True:
    bet = float(input("\nHow much money do you want to bet ? "))
    print("")
    if bet > balance:
        print("\nYou don't have enough money to bet that much !")
        continue
    else:
        balance -= bet
        break

while True:

    if balance <= 0:
        break
    
    player_hand = functions.get_hand(deck)
    player_hand_value = functions.get_value(player_hand)

    dealer_hand = functions.get_hand(deck)
    dealer_hand_value = functions.get_value(dealer_hand)

    if "A" in player_hand and player_hand_value > 21:
        player_hand_value -= 10

    if "A" in dealer_hand and dealer_hand_value < 21:
        dealer_hand_value += 10
        
    
    functions.game_menu(balance, bet,dealer_hand, dealer_hand_value, player_hand, player_hand_value)
    
        
    if player_hand_value == 21:
        print("\nYou got Blackjack!")
        balance += bet * 1.5
        print(balance)
        continue
    
    if dealer_hand_value == 21:
        print("\nDealer got Blackjack!")
        balance -= bet
        print(balance)
        
        continue
    
    choice = input("\nDo you want to hit or stand ?")
    
    if choice.lower() == "hit":
        while True:
            player_hand.append(random.choice(deck))
            player_hand_value = functions.get_value(player_hand)
            if "A" in player_hand and player_hand_value > 21:
                player_hand_value -= 10
                
            functions.game_menu(balance, bet,dealer_hand, dealer_hand_value, player_hand, player_hand_value)
            
            if player_hand_value > 21:
                print("You busted!")
                balance -= bet
                break
            elif player_hand_value == 21:
                print("You got Blackjack!")
                balance += bet * 1.5
                break
            else:
                choice = input("\nDo you want to hit or stand ? ")
                if choice.lower() == "stand":

                    break
                
                
    close_21_player = 21 - player_hand_value
    close_21_dealer = 21 - dealer_hand_value
    
    if close_21_dealer < close_21_player and dealer_hand_value < 21:
        print("\nDealer wins!")
        balance -= bet
        
    if close_21_player < close_21_dealer and player_hand_value < 21:
        print("\nYou win!")
        balance += 1.5 * bet
        
    print("Your balance is now " + str(balance))
        
    if balance <= 0:
        print("\nYou don't have enough money to play anymore !")
        balance = 0
    
    bet = float(input("\nHow much money do you want to bet ? "))
    
    if bet > balance:
        print("\nYou don't have enough money to bet that much !")
        bet = float(input("\nHow much money do you want to bet ? "))
        continue
        
    

































