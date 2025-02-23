"""Absences at Work
Program to keep track of absences of employees - v3
function to find person with most days absent
Created by Charlotte"""

# at_childcare.index(child_)

def average_absent():
    average_days = sum(employee_days) / len(employee_days)
    print(f"Average number of days staff were absent: {average_days:.1f}")

def person_most_absent():
    most_days = max(employee_days)
    index = employee_days.index(most_days)
    person = employee_names_joined[index]
    print(f"Person with most days absent: {person} with {most_days} days")

# Main routine
employee_names_unjoined = []
employee_names_joined = []
employee_days = []

while True:
    employee_names_days = input("Input employee full name and number of days absent: ").split()
    if employee_names_days == ['$']:
        break
    employee_names_unjoined.append(employee_names_days [0])
    employee_names_unjoined.append(employee_names_days [1])
    # joins just the two names into one string
    names_joined = " ".join(employee_names_unjoined)
    # appends full name as one string into all names list
    employee_names_joined.append(names_joined)
    # turns str number into integer
    days = int(employee_names_days [2])
    employee_days.append(days)
    print(employee_names_joined)
    print(employee_days)
    employee_names_unjoined.clear()
average_absent()
person_most_absent()
