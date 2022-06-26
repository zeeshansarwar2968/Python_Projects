"""
6. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""
"""
solved by : Zeeshan Sarwar
"""

import datetime

# Initialising the data points provided for the program
date1 = datetime.date(2014, 7, 2)
date2 = datetime.date(2014, 7, 11)

"""
Using the date class in datetime module to take the input in proper syntax as follows
class date(builtins.object)
 |  date(year, month, day) --> date object
"""
days_diff = date2-date1
print(days_diff.days, "days")

# print(help(datetime.date))
# print(help(datetime))
# print(date2-date1)
