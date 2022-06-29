"""
 2. Write a Python program to iteration over sets.
"""
# Solved by Zeeshan Sarwar

user_input = input("Please provide the count of user input : ")

try:
    size_list = int(user_input)
    print("Please provide the elements for the set : ")
    list_data = [int(input("Element : ")) for i in range(size_list)]
    set_data = set(list_data)
    for i in set_data: print(f"Set Element : {i}")
except ValueError:
    print("Please Provide numeric Input")