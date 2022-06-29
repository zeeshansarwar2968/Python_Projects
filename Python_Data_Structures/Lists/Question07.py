"""
7. Write a Python program to clone or copy a list.
"""
# Solved by Zeeshan Sarwar

user_input = input("Please provide the size of the list : ")

try:
    size_list = int(user_input)
    print("Please provide the elements of the list : ")
    list_data = [int(input("Element : ")) for i in range(size_list)]
    list_copy = list_data.copy()
    print(f"The original list : {list_data}")
    print(f"The copied list : {list_copy}")

except ValueError:
    print("Please Provide numeric Input")
