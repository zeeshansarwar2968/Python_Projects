"""
14.Write a Python program to list all files in a directory in Python.
"""
"""
solved by : Zeeshan Sarwar
"""
import os

"""
Syntax: os.listdir(path)

Parameters:

Path of the directory
Return Type: returns a list of all files and directories in the specified path
"""
path = "C:/Users/zeesh/Desktop/CFP/Python/Python_Projects/Basic_Python_Problems"
# print(help(os.listdir))
list_dir = os.listdir(path)
for i in range(len(list_dir)):
    print(f"{i} : {list_dir[i]}")
# print(os.listdir(path))
