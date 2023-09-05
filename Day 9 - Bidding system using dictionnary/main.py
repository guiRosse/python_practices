import os
from logo import logo

is_bidding = "y"
bidder = ""
bid = 0
max_bid = 0
max_bidder = ""

bid_dict = {}

def cls():
    os.system('cls')

cls()

while is_bidding.lower() in ["yes","y"]:
    print(logo)
    bidder = input("What's your name: ")
    bid = int (input("What's your bid: "))

    bid_dict[bidder] = bid
    print(bid_dict)
    is_bidding = input("Is there another bidder? Type Yes or No : ")

    if is_bidding.lower() in ["yes","y"]:
        cls()
    else:
        cls()
        for bidder in bid_dict:
            if bid_dict[bidder] > max_bid:
                max_bid = bid_dict[bidder]
                max_bidder = bidder

cls()
print(f"Congrats to {max_bidder.capitalize()}. You won the bid with ${max_bid}!!")