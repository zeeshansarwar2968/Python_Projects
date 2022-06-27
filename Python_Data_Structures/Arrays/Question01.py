"""
1. Write a Python program to create an array of 5 integers and display the array items.
Access individual element through indexes.
"""
# Solved by Zeeshan Sarwar

list_elements = []

try:
    print("Please Provide the elements of the array : ")
    list_elements = [int(input("Element : ")) for i in range(5)]

    for i in range(5): print(f"element {i + 1} : {list_elements[i]}")

except ValueError:
    print("Please Provide Numeric Input")

