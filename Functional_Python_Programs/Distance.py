# Write a program Distance.java that takes two integer command-line arguments x
# and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
# formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function

import math  # importing math library to use math.pow and sqrt method/function

# Taking in user inputs for the x and y axes
user_input1 = input("Please input the first argument (x) : ")
user_input2 = input("Please input the second argument (y) : ")

try:
    x = int(user_input1)    # explicit type casting of input value to integer
    y = int(user_input2)    # explicit type casting of input value to integer

    # implementation of the euclidean formula to calculate the distance
    euclidean_distance = math.sqrt(abs(math.pow(x, 2) + math.pow(y, 2)))

    # Printing the output using f-string to dynamically insert the required values
    print(f"The Euclidean distance from point ({x},{y}) to (0,0) is : {euclidean_distance}")

except ValueError:
    print("Please provide numeric values")



