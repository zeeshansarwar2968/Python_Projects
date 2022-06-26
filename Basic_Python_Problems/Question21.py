"""
21. Write a Python program to sort files by date.
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

# If a key function is given, apply it once to each list item and sort them,
# ascending or descending, according to their function values.
list_dir.sort(key=lambda x: os.path.getmtime(x))
for i in range(len(list_dir)):
    print(f"{i} : {list_dir[i]}")
