"""Taxi Trips
Program to keep track of details for a taxi - v1
code without error check
Created by Charlotte"""

name = input("Enter driver's name: ").title()
total_minutes = 0
total_trips = 0
total_cost = 0
new_trip = "Yes"
while new_trip == "Yes":
    total_trips += 1
    minutes = float(input("Enter length of trip in minutes: "))
    total_minutes += minutes
    cost = 10 + 2*minutes
    print(f"This trip cost ${cost:.2f}")
    total_cost += cost
    new_trip = input("Do you want a new trip? Enter 'Yes' or 'No': ").title()
    print()
print("=" * 60)
average_time = total_minutes / total_trips
average_income = total_cost / total_trips
print(f"Driver {name} had {total_trips} trips totalling {total_minutes} minutes.")
print(f"The average time of all the trips was {average_time} minutes")
print(f"The total income for the day was ${total_cost}")
print(f"The average income for each trip was ${average_income}")
