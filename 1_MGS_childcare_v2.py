"""MGS Childcare
Program for child day-care centre - version 1 - main function
created by Charlotte"""

def drop_off():
    name_ = input("Please enter the name of the child: ").title()
    roll.append(name_)
    print(f"\n{name_} has been added to the roll.\n")

# Main routine
roll = []
choice = 0

while choice != 5:
    print("=" * 60)
    print("What would you like to do?")
    print("=" * 60)
    print()
    print("1 Drop off a child")
    print()
    choice = int(input("Enter your choice (number from 1 to 5): "))
    print()

    if choice == 1:
        drop_off()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    else:
        print("Goodbye")
