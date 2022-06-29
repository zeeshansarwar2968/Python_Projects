"""
1.    Write a Python program to create a tuple.
"""
# Solved by Zeeshan Sarwars

user_input = input("Please provide the count of user input : ")

try:
    size_list = int(user_input)
    print("Please provide the elements for the set : ")
    list_data = [int(input("Element : ")) for i in range(size_list)]
    print(f"The Set : {set(list_data)}")
except ValueError:
    print("Please Provide numeric Input")