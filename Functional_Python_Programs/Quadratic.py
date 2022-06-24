# Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
# Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
# can be found using a formula
# delta = b*b - 4*a*c
# Root 1 of x = (-b + sqrt(delta))/(2*a)
# Root 2 of x = (-b - sqrt(delta))/(2*a)
# Take a, b and c as input values to find the roots of x.

import math     # importing math library to use math.sqrt method/function

# Taking in user inputs for the a,b and c values
user_input1 = input("Please input the value of a : ")
user_input2 = input("Please input the value of b : ")
user_input3 = input("Please input the value of c : ")

try:
    # explicit type casting of input value to integer
    a = int(user_input1)
    b = int(user_input2)
    c = int(user_input3)

    # Implementing the provided formulas in python
    delta = b*b - 4*a*c
    root1 = ((-b) + math.sqrt(abs(delta)))/(2*a)
    root2 = ((-b) - math.sqrt(abs(delta)))/(2*a)

    # Printing the output root values to console
    print(f"The first root of x is : {root1}")
    print(f"The second root of x is : {root2}")

except ValueError:
    print("Provide proper inputs")