"""Silent Auction
Program to take care of a silent auction
getting started
Created by Charlotte"""

item = input("Enter the item you want to sell: ")
reserve_price = float(input("Enter the reserve price $ "))
bid = 0
highest_bid = 0
while bid != -1:
    print(f"Highest bid so far is ${highest_bid}")
    bid = float(input("Enter your bid $"))