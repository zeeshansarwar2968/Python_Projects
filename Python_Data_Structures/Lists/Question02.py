"""
Question-02;
Write a Python program to multiplies all the items in a list.
"""
# Solved by Zeeshan Sarwar

from functools import reduce

user_input = input("Please provide the size of the list : ")

try:
    size_list = int(user_input)
    print("Please provide the elements of the list : ")
    list_data = [int(input("Element : ")) for i in range(size_list)]
    multiplied = reduce(lambda a, b: a*b, list_data)

    print(f"The multiplication of the elements in the list is : {multiplied}")
except ValueError:
    print("Please Provide numeric Input")
