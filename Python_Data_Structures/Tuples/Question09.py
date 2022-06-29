"""
9.  Write a Python program to slice a tuple.
"""
# Solved by Zeeshan Sarwar

user_input = input("Please provide the count of user input : ")

try:
    size_list = int(user_input)
    print("Please provide the elements for the tuple : ")
    list_data = [input("Element : ") for i in range(size_list)]
    sample_tuple = tuple(list_data)
    print(f"The original tuple is : {sample_tuple}")
    to_slice = int(input("Please provide the element count to slice from tuple from the beginning : "))
    updated_tuple = sample_tuple[:to_slice]
    print(f"The sliced tuple is : {updated_tuple}")
except ValueError:
    print("Please Provide numeric Input")