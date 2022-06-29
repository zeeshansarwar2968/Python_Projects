"""
7.  Write a Python program to convert a list to a tuple.
"""

# Solved by Zeeshan Sarwar

user_input = input("Please provide the count of user input : ")

try:
    size_list = int(user_input)
    print("Please provide the elements for the tuple : ")
    list_data = [int(input("Element : ")) for i in range(size_list)]

    sample_tuple = tuple(list_data)
    print(f"The Tuple is : {sample_tuple} of type : {type(sample_tuple)}")
except ValueError:
    print("Please Provide numeric Input")