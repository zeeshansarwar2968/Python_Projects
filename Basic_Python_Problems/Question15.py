"""
15. Write a python program to access environment variables.
"""
"""
solved by : Zeeshan Sarwar
"""
import os

"""
The os.environ variable is a dictionary-like object. If we print it, all the environment variables 
name and values will get printed.
"""
print("-----------------------------------------------------------------------------------------------")
print("Printing the value stored for the env variable 'SYSTEMDRIVE' : ",os.environ['SYSTEMDRIVE'])
list_dir = os.environ

print("-----------------------------------------------------------------------------------------------")

print("")
for i in list_dir:
    print(f"{i} : {list_dir[i]}")



# print(list_dir)