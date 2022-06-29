"""
6. Write a Python program to remove duplicates from a list.
"""
# Solved by Zeeshan Sarwar

user_input = input("Please provide the size of the list : ")

try:
    size_list = int(user_input)
    print("Please provide the elements of the list : ")
    list_data = [int(input("Element : ")) for i in range(size_list)]
    print(f"The list with unique values : {list(set(list_data))}")
except ValueError:
    print("Please Provide numeric Input")