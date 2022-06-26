"""
5. Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
"""
"""
solved by : Zeeshan Sarwar
"""
import calendar

try:
    month = int(input("Please enter the month in numeric format ( 1 to 12) : "))
    year = int(input("Please enter the year : "))

    """
    calendar.monthcalendar : 
    Return a matrix representing a month's calendar.
    Each row represents a week; days outside this month are zero.
    """
    calender_info = calendar.monthcalendar(year, month)

    # print(type(calender_info))
    # print(help(calendar.monthcalendar))

    for i in range(len(calender_info)):
        print(f"Week-0{i + 1} : {calender_info[i]}")

except ValueError:
    print("Please enter a valid numeric value")

