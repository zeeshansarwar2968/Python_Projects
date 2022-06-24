# Write a program WindChill.java that takes two double command-line arguments t
# and v and prints the wind chill. Use Math.pow(a, b) to compute ab.
# Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour),
# the National Weather Service defines the effective temperature (the wind chill) to
# be:

# Note : the formula is not valid if t is larger than 50 in absolute value or if v is larger
# than 120 or less than 3 (you may assume that the values you get are in that range).

import math

user_input1 = input("Please input the value of temperature (in Fahrenheit between 0 and 50) : ")
user_input2 = input("Please input the value of wind speed (in miles per hour between 3 and 120) : ")
try:
    t = float(user_input1)
    v = float(user_input2)

    if 0 <= t <= 50 and 3 <= v <= 120:
        windchill = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
        print(f"The Effective Temperature (wind chill) is : {windchill}")
    else:
        print("Please provide the input in given range")

except ValueError:
    print("Please provide numeric value")
