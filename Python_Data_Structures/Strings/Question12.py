"""
12. Write a Python program to lowercase first n characters in a string.
"""
# Solved by Zeeshan Sarwar


def lwr_firstn(stringdata, n):
    """
    This is a function to lowercase first n characters in a string
    :param stringdata: string
    :param n: int
    :return: string
    """
    return stringdata[:n].lower()+stringdata[n:]


try:
    strData = input("Please provide the string : ")
    N = int(input("Please provide the value of N : "))
    str_temp = lwr_firstn(strData, N)
    print(f"The required string is : {str_temp}")
except ValueError:
    print("Please input numeric values")
