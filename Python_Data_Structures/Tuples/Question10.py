"""
10. Write a Python program to reverse a tuple.
"""
# Solved by Zeeshan Sarwar

user_input = input("Please provide the count of user input : ")

try:
    size_list = int(user_input)
    print("Please provide the elements for the tuple : ")
    list_data = [input("Element : ") for i in range(size_list)]
    sample_tuple = tuple(list_data)
    print(f"The original tuple is : {sample_tuple}")
    list_data.reverse()
    reversed_tuple = tuple(list_data)
    print(f"The sliced tuple is : {reversed_tuple}")
except ValueError:
    print("Please Provide numeric Input")
