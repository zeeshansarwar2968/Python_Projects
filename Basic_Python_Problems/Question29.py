"""
29. Write a Python program to get the name of the host on which the routine is running.
"""
# Solved by Zeeshan Sarwar

import os

"""
The os.environ variable is a dictionary-like object. If we print it, all the environment variables 
name and values will get printed.
"""
print("-----------------------------------------------------------------------------------------")
print("Printing the name of the host on which the routine is running : ", os.environ['COMPUTERNAME'])
# list_dir = os.environ

print("-----------------------------------------------------------------------------------------")

# print("")
# for i in list_dir:
#     print(f"{i} : {list_dir[i]}")
