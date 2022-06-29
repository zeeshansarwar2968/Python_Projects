"""
3. Write a Python program to add member(s) in a set.
"""
# Solved by Zeeshan Sarwar

user_input = input("Please provide the count of user input : ")

try:
    size_set = int(user_input)
    print("Please provide the elements for the set : ")
    set_data = set()
    for i in range(size_set): set_data.add(int(input("Set element : ")))
    print(f"Final Set : {set_data}")
except ValueError:
    print("Please Provide numeric Input")