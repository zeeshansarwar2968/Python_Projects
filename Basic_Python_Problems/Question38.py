"""
38. Write a Python program to add leading zeroes to a string.
"""
# Solved by Zeeshan Sarwar

user_input = input("Please input the string : ")
user_input_int = input("Please inout the count of leading zeroes to be added : ")

temp_string = user_input
try:
    zero_count = int(user_input_int)

    for i in range(zero_count):
        temp_string = "0" + temp_string

    print(temp_string)
except ValueError:
    print("Please provide numeric values")
