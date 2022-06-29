"""
1.    Write a Python program to create a tuple.
"""
# Solved by Zeeshan Sarwar

user_input = input("Please provide the count of user input : ")

try:
    size_list = int(user_input)
    print("Please provide the elements for the tuple : ")
    list_data = [int(input("Element : ")) for i in range(size_list)]

    sample_tuple = tuple(list_data)
    print(f"The Tuple is : {sample_tuple}")
    # print(f"The set is : {set(list_data)}")

except ValueError:
    print("Please Provide numeric Input")