def find_highest_bid(bidding_dictionary):
    winner=""
    highest_bid=0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]   
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid amount {highest_bid}")

from logos import logo
import os
print(logo)
print("Welcome to secret Auction program\n")
bids={}
program_continue = True
while program_continue == True:
    name = input("Enter your name:")
    bid_price = int(input("What is your bid?: $"))
    bids[name] = bid_price
    should_continue=input("Are there any other bidders?Type yes or no\n").lower()
    if should_continue == 'no':
        program_continue = False
        find_highest_bid(bids)
    
    if program_continue == True:
       os.system('cls')
print("Thank You")
    