"""Absences at Work
Program to keep track of absences of employees - v2
function to find average number of days staff absent
Created by Charlotte"""

# at_childcare.index(child_)

def average_absent():
    average_days = sum(employee_days) / len(employee_days)
    print(f"Average number of days staff were absent: {average_days}")

# Main routine
employee_names_unjoined = []
employee_names_joined = []
employee_days = []

while True:
    employee_names_days = input("Input employee full name and number of days absent: ").split()
    if employee_names_unjoined == "$":
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
