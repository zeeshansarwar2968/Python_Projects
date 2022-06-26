"""
9. Write a Python program to concatenate all elements in a list into a string and return it.
"""
"""
solved by : Zeeshan Sarwar
"""


def string_converter(list_value):
    """
    Concatenates all elements in a list into a string and return it.
    :param list_value: list
    :return: string
    """
    return " ".join(list_data)


list_size = int(input("Please specify the size of list : "))

list_data = list()
print("Please provide the elements for the list. --> ")
for i in range(list_size):
    temp = input("Element : ")
    list_data.append(temp)
print(f"The list is : {list_data}")
print(f"The Concatenated string is : {string_converter(list_data)}")

