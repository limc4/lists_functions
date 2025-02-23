"""Speeding motorists and warrants
Program to calculate fines for speeders
list of wanted speeders
Created by Charlotte"""

def calc_fine():
    speed = int(input("Enter the amount over the speed limit: "))
    if speed >= 45:
        fine = 630
    elif speed >= 40:
        fine = 510
    elif speed >= 35:
        fine = 400
    elif speed >= 30:
        fine = 300
    elif speed >= 25:
        fine = 230
    elif speed >= 20:
        fine = 170
    elif speed >= 15:
        fine = 120
    elif speed >= 10:
        fine = 80
    else:
        fine = 30
    return fine

def check_wanted(question):
    wanted_ = ["James Wilson", "Helga Norman", "Zachary Conroy"]
    name_ = input(question).title()
    if name_ in wanted_:
        print(f"{name_.capitalize()} - WARRANT TO ARREST")
    return name_

# Main routine
wanted = ["James Wilson", "Helga Norman", "Zachary Conroy"]
name = (check_wanted("Enter name: "))
# name = check_wanted(input("Enter the speeder's full name: "))
print(f"{name} to be fined ${calc_fine()}")
