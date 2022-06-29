"""
6.  Write a Python program to check whether an element exists within a tuple.
"""
# Solved by Zeeshan Sarwar


def check_tuple(element, tupledata):
    """
    return true if element in present in the tuple
    :param element: element
    :param tupledata: tuple
    :return: boolean
    """
    return element in tupledata


user_input = input("Please provide the count of user input : ")
size_list = int(user_input)
print("Please provide the elements for the tuple : ")
list_data = [input("Element : ") for i in range(size_list)]
sample_tuple = tuple(list_data)

check_element = input("Please provide the element to check presence in the tuple : ")
print(f"\nIs the element {check_element} present in the tuple : {check_tuple(check_element, sample_tuple)}")
