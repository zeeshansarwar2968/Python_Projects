"""
1.   Write a Python program to calculate the length of a string.
"""
# Solved by Zeeshan Sarwar


def string_length(stringdata):
    """
    Retuns the length of a string
    :param stringdata: string value
    :return: size of stringdata(int)
    """
    return len(stringdata)


user_input = input("Please provide a string to find its length : ")

print(f"The length of the input string data is : {string_length(user_input)}")
