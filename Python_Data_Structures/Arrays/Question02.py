"""
2. Write a Python program to reverse the order of the items in the array.
"""
# Solved by Zeeshan Sarwar


print("Please Provide the elements of the array : ")
try:
    list_elements = [int(input("Element : ")) for i in range(5)]
    list_elements.reverse()
    print(list_elements)
except ValueError:
    print("Please Provide Numeric Inputs")

