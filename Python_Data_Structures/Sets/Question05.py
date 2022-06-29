"""
 5. Write a Python program to remove an item from a set if it is present in the set.
"""
# Solved by Zeeshan Sarwar

user_input = input("Please provide the count of user input : ")

try:
    size_set = int(user_input)
    print("Please provide the elements for the set : ")
    set_data = set()
    for i in range(size_set): set_data.add(int(input("Set element : ")))
    print(f"Final Set : {set_data}")
    to_delete = int(input("\nPlease specify the element to delete : "))
    # set_data.remove(to_delete) if to_delete in set_data else print(f"Element : {to_delete} is not present in the set")
    set_data.discard(to_delete)
    print(f"Set : {set_data}")

except ValueError:
    print("Please Provide numeric Input")
