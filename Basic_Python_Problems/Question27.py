"""
27. Write a Python program to get the system time.
"""
"""
solved by : Zeeshan Sarwar
"""

import datetime

"""
now(tz=None) method of builtins.type instance
    Returns new datetime object representing current time local to tz.
"""

print(f"The current System time is : {datetime.datetime.now()} ")

print(help(datetime.datetime.now))