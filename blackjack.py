import random
import os
from logos import logo
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score ,c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose,opponent has Blackjack"
    elif u_score == 0:
        return "You Win with a BlackJack"
    elif u_score > 21:
        return "You went over,You lose"
    elif c_score > 21:
        return "Opponent went over,You Win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You lost"

def play_game():
    os.system('cls')
    print(logo)
    user_card = []
    computer_card = []
    computer_score = -1
    user_score =-1
    is_game_over = False

    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your cards:{user_card},current score:{user_score}")
        print(f"Computer's first card:{computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal=input("type 'y' to get another card,Type 'n' to pass :")
            if user_should_deal=='y':
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score !=0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"Your final hand :{user_card},Final score:{user_score}")
    print(f"Computer's final hand :{computer_card},Final score:{computer_score}")
    print(compare(user_score,computer_score))
    print("\n")

playgame = True
while playgame:
    play=input("Do you want to play a game of BlackJack? type 'y' or 'n':")
    if play == 'y':  
        playgame = True
    else:
        playgame = False
    if playgame == False:
        break
    play_game()