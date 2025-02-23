"""Absences at Work
Program to keep track of absences of employees - v4
function to find people with no days absent
Created by Charlotte"""

# at_childcare.index(child_)

def average_absent():
    average_days = sum(employee_days) / len(employee_days)
    print(f"Average number of days staff were absent: {average_days:.2f} days")

def person_most_absent():
    most_days = max(employee_days)
    index = employee_days.index(most_days)
    person = employee_names_joined[index]
    print(f"Person with most days absent: {person} with {most_days} days")

def list_no_absent():
    for first, last, absences in name_day:
        absences = int(absences)
        if absences == 0:
            result = [f"{first} {last}"]
    # alphabetical = sorted(result)
    # print(alphabetical)
            all_0.append(result)

    print("\nemployees with no absences:")
    if not all_0:
        print("none")
    else:
        all_0.sort()
        for name in all_0:
            print(name)

# Main routine
employee_names_unjoined = []
employee_names_joined = []
employee_days = []
name_day = []
all_0 = []

while True:
    employee_names_days = input("Input employee full name and number of days absent: ").split()
    if employee_names_days == ['$']:
        break
    employee_names_unjoined.append(employee_names_days [0])
    employee_names_unjoined.append(employee_names_days [1])
    name_day.append(employee_names_days)
    # joins just the two names into one string
    names_joined = " ".join(employee_names_unjoined)
    # appends full name as one string into all names list
    employee_names_joined.append(names_joined)
    # turns str number into integer
    days = int(employee_names_days [2])
    employee_days.append(days)

    employee_names_unjoined.clear()
average_absent()
person_most_absent()
list_no_absent()
