"""MGS Childcare
Program for child day-care centre - version 4 - pick up function included
function to calculate cost
created by Charlotte
"""

# def drop_off():
#     name_ = input("Please enter the name of the child: ").title()
#     at_childcare.append(name_)
#     print(f"\n{name_} has been added to the roll.\n")
#
# def pick_up():
#     valid = at_childcare
#     child_ = input("Please enter the name of the child you wish to pick up: ").title()
#     while child_ not in valid:
#         print("\nThat child doesn't seem to be in the roll. ")
#         child_ = input("Please check spelling, or enter another name: ").title()
#     at_childcare.pop(at_childcare.index(child_))
#     print(at_childcare)
#     print(f"{child_} has been picked up.")

def calc_cost():
    cost_hours = 12
    hours_ = int(input("Enter the number of hours that the children have attended today: "))
    cost_ = len(at_childcare) * hours_ * cost_hours
    print(f"The cost for looking after {len(at_childcare)} children for {hours_} hours is ${cost_}")

# Main routine
at_childcare = ["Jeremy", "Chloe"]
choice = 0

# while choice != 5:
#     print("=" * 60)
#     print("What would you like to do?")
#     print("=" * 60)
#     print()
#     print("1 Drop off a child")
#     print("2 Pick up a child")
#     print()
#     choice = int(input("Enter your choice (number from 1 to 5): "))
#     print()
#
#     if choice == 1:
#         drop_off()
#     elif choice == 2:
#         pick_up()
#     elif choice == 3:
#         pass
#     elif choice == 4:
#         pass
#     else:
#         print("Goodbye")
calc_cost()
