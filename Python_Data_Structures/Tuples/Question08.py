"""
8.  Write a Python program to remove an item from a tuple.
"""
# Solved by Zeeshan Sarwar

user_input = input("Please provide the count of user input : ")

try:
    size_list = int(user_input)
    print("Please provide the elements for the tuple : ")
    list_data = [input("Element : ") for i in range(size_list)]
    sample_tuple = tuple(list_data)
    print(f"The original tuple is : {sample_tuple}")
    to_remove = input("Please provide the element to remove from tuple : ")
    index1 = sample_tuple.index(to_remove)
    updated_tuple = sample_tuple[:index1] + sample_tuple[index1+1:]
    print(f"The updated tuple is : {updated_tuple}")
except ValueError:
    print("Please Provide numeric Input")