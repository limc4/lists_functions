"""Speeding motorists and warrants
Program to book vehicles - v1
vehicle options and seats needed
Created by Charlotte"""

def seats_cars():
    seats_needed_ = int(input("Enter the number of seats needed: "))
    print("Car number   car type    number of seats\n")
    for number, vehicle, seats in vehicles:
        print(f"{number})   {vehicle}   {seats}")
        seats = int(seats)
        if seats < seats_needed_:
            print("Not enough seats")


# Main routine
vehicles = [["1", "Suzuki Van", "2"], ["2", "Toyota Corolla", "4"], ["3",
"Honda CRV", "4"], ["5", "Mitsubishi Airtrek", "4"], ["6", "Nissan DC Ute",
"4"], ["7", "Toyota Previa", "7"], ["8", "Toyota Hi Ace", "12"], ["9",
"Toyota Hi Ace", "12"]]
cars = []
seats_cars()
