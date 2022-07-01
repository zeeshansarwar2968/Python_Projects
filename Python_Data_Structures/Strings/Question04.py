"""
4. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
    If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
    given string is less than 3, leave it unchanged.
    Sample String : 'abc'
    Expected Result : 'abcing'
    Sample String : 'string'
    Expected Result : 'stringly'
"""
# Solved by Zeeshan Sarwar


def string_concat(string):
    """
    returns a new string based on the conditional block
    :param string: string
    :return: string
    """
    return string+'ly' if string.endswith('ing') else string+'ing'


user_input = input("Please provide a string to change its verb : ")
print(f"The final string is : {string_concat(user_input)}")
