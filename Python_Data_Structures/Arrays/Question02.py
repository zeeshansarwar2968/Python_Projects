"""
2. Write a Python program to reverse the order of the items in the array.
"""
# Solved by Zeeshan Sarwar

import array

print("Please Provide the elements of the array : ")
try:
    list_elements = [int(input("Element : ")) for i in range(5)]
    array_data = array.array('i', list_elements)
    print("Original Array:", array_data)
    array_data.reverse()
    print("Reversed Array:", array_data)
except ValueError:
    print("Please Provide Numeric Inputs")

