"""
18. Write a Python program to get an absolute file path.
"""
"""
solved by : Zeeshan Sarwar
"""
import os



def abs_file_path(path_info):
    """
    Returns the absolute path
    :param path_info: path string
    :return: file path
    """
    return os.path.abspath(path_info)


user_input = input("Please provide the file name to view the absolute path : ")

path_value = abs_file_path(user_input)

print(f"The path is : {path_value}")
