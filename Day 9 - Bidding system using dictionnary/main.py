import os
from logo import logo

is_bidding = "y"
bidder = ""
bid = 0
bid_dict = {}

def cls():
    os.system('cls')

def find_highest_bid(bids):
    max_bid = 0
    max_bidder = ""
    for bidder in bids:
        if bids[bidder] > max_bid:
            max_bid = bids[bidder]
    
    max_bidder = bidder
    return max_bidder

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
        max_bidder = find_highest_bid(bid_dict)
        max_bid = bid_dict[max_bidder]

cls()
print(f"Congrats to {max_bidder.capitalize()}. You won the bid with ${max_bid}!!")