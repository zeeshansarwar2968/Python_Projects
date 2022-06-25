# Simulate Stopwatch Program
# a. Desc -> Write a Stopwatch Program for measuring the time that elapses between
# the start and end clicks
# b. I/P -> Start the Stopwatch and End the Stopwatch
# c. Logic -> Measure the elapsed time between start and end
# d. O/P -> Print the elapsed time.

import time     # importing the time module to record the time information in stopwatch calculation

try:
    while True:
        start = int(input("Please Enter 1 to Start : "))
        # time.time() methods return the current time in seconds since epoch.
        # It returns a floating-point number.
        startTime = time.time()     # Current time in seconds since epoch
        stop = int(input("Enter 0 to Stop Time : "))
        endTime = time.time()       # Current time in seconds since epoch
        timeElapsed = endTime - startTime   # Here we are subtracting the latest time by the last recorded time
        print(f"Time elapsed from Start to Stop is : {timeElapsed} seconds");
        print(f"The current time is : {time.ctime()}")
except ValueError:
    print("Invalid input, Please enter either 1 or 0 to start/stop the stopwatch")