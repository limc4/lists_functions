"""Silent Auction
Program to take care of a silent auction - v2
check if highest bid meets reserve
Created by Charlotte"""

def check_higher_lower_highest():
    bid_ = bid
    while bid_ <= highest_bid:
        if bid_ == -1:
            return bid_
        print(f"Your bid must be higher than ${highest_bid}")
        bid_ = float(input("Please enter your bid $ "))
    return bid_

def check_meets_reserve():
    end_bid = highest_bid
    if end_bid < reserve_price:
        print()
        print(f"The {item} didn't sell because the reserve price was not met.")
    else:
        print(f"\nThe {item} sold for ${highest_bid:.2f}!!")

# Main routine
item = input("Enter the item you want to sell: ")
reserve_price = float(input("Enter the reserve price $ "))
print(f"\nThe auction for {item} has started! \n")
bid = 0
highest_bid = 0
while bid != -1:
    print(f"Highest bid so far is ${highest_bid}")
    bid = float(check_higher_lower_highest())
    if bid != -1:
        highest_bid = bid
print(highest_bid)
check_meets_reserve()
