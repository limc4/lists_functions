"""Speeding motorists and warrants
Program to book vehicles - v3
stop loop when no more vehicles or when -1 entered
Created by Charlotte"""

def seats_cars():
    seats_needed_ = int(input("Enter the number of seats needed: "))
    if seats_needed_ == -1:
        return seats_needed_
    print("Car number   car type    number of seats\n")
    for number, vehicle, seats in vehicles:
        print(f"{number})   {vehicle}   {seats}")
        seats = int(seats)
        if seats < seats_needed_:
            print("Not enough seats")
    return seats_needed_

def book_car():
    number_ = int(input("Enter the number of the vehicle you'd like to book: "))
    index = 0
    for number, vehicle, seats in vehicles:
        num = int(number)
        if number_ == num:
            name = input("Enter your name: ")
            booked_vehicles.append(number)
            booked_vehicles.append(vehicle)
            booked_vehicles.append(seats)
            booked_vehicles.append(name)
            # print(booked_vehicles)
            # print(vehicles)
            # print(number)
            vehicles.pop(index)
            # print(vehicles)
        index += 1

def print_summary():
    index = 0
    # print(booked_vehicles)
    while index < len(booked_vehicles):
        # booked_vehicles:
        print(f"{booked_vehicles[index]})    {booked_vehicles[index+1]}   Booked by: {booked_vehicles[index+3]}")
        index += 4


# Main routine
vehicles = [["1", "Suzuki Van", "2"], ["2", "Toyota Corolla", "4"], ["3",
"Honda CRV", "4"], ["4", "Suzuki Swift", "4"], ["5", "Mitsubishi Airtrek", "4"], ["6", "Nissan DC Ute",
"4"], ["7", "Toyota Previa", "7"], ["8", "Toyota Hi Ace", "12"], ["9",
"Toyota Hi Ace", "12"]]
booked_vehicles = []
cars = []
while True:
    if not vehicles:
        break
    if seats_cars() == -1:
        break
    book_car()
print()
print("Cars booked:")
print_summary()
