"""Silent Auction
Program to take care of a silent auction - v2
getting started - check if bid is higher than the highest bid
Created by Charlotte"""

def check_higher_lower():
    bid_ = bid
    while bid_ <= highest_bid:
        print(f"Your bid must be higher than ${highest_bid}")
        bid_ = float(input("Please enter your bid $ "))
    return bid_

# Main routine
item = input("Enter the item you want to sell: ")
reserve_price = float(input("Enter the reserve price $ "))
bid = 0
highest_bid = 0
while bid != -1:
    print(f"Highest bid so far is ${highest_bid}")
    bid = float(check_higher_lower())
    highest_bid = bid
