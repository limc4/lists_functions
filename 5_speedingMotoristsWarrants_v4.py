"""Speeding motorists and warrants
Program to calculate fines for speeders - v4
total number of fines + fine amount
Created by Charlotte"""

def calc_fine():
    speed = int(input("Enter the amount over the speed limit: "))
    if speed >= 45:
        fine_ = 630
    elif speed >= 40:
        fine_ = 510
    elif speed >= 35:
        fine_ = 400
    elif speed >= 30:
        fine_ = 300
    elif speed >= 25:
        fine_ = 230
    elif speed >= 20:
        fine_ = 170
    elif speed >= 15:
        fine_ = 120
    elif speed >= 10:
        fine_ = 80
    else:
        fine_ = 30
    return fine_

def check_wanted(question):
    wanted_ = ["James Wilson", "Helga Norman", "Zachary Conroy"]
    name_ = input(question).title()
    if name_ in wanted_:
        print(f"{name_.capitalize()} - WARRANT TO ARREST")
    return name_

# Main routine
total_fines = 0
total_fine_amount = 0
wanted = ["James Wilson", "Helga Norman", "Zachary Conroy"]
name = ""
people = []
fines = []
while True:
    name = (check_wanted("Enter name (or enter 'X' to quit): ").title())
    if name == "X":
        break
    people.append(name)
    fine = calc_fine()
    total_fine_amount += fine
    fines.append(fine)
    print(f"{name} to be fined ${fine}")
    total_fines += 1
print(f"Total fines: {total_fines}")
print(f"Total fine amount: ${total_fine_amount}")


