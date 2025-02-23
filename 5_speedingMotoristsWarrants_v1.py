"""Speeding motorists and warrants
Program to calculate fines for speeders - v1
get name and speed and calculate fine
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

# Main routine
name = input("Enter the speeder's name: ").title()
print(f"{name} to be fined ${calc_fine()}")
