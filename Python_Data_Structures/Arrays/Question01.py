"""
1. Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
"""
# Solved by Zeeshan Sarwar
import array

list_elements = []

try:
    print("Please Provide the elements of the array : ")
    list_elements = [int(input("Element : ")) for i in range(5)]
    array_data = array.array('i', list_elements)
    for i in range(len(array_data)): print(f"element {i + 1} : {array_data[i]}")

except ValueError:
    print("Please Provide Numeric Input")

