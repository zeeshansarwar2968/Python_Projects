"""
11. Write a Python program to check whether a file exists.
"""
"""
solved by : Zeeshan Sarwar
"""
import os.path

"""
OS module in Python provides functions for interacting with the operating system. 
OS comes under Python’s standard utility modules. This module provides a portable way of using operating system 
dependent functionality. os.path module is sub module of OS module in python used for common path name manipulation.

Syntax: os.path.exists(path)

Parameter:
path: A path-like object representing a file system path. A path-like object is either a string or bytes object 
representing a path.

Return Type: This method returns a Boolean value of class bool. This method returns True if path exists otherwise 
returns False.
"""
path1 = "/Users/zeesh/Desktop/CFP/Python/Python_Projects/Basic_Python_Problems/Question08.py"
file_path = "README.md"

print(f"file : {os.path.exists(path1)}")
print(f"file2 : {os.path.exists(file_path)}")
