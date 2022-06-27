"""
36. Write a Python program to determine if variable is defined or not.
"""
# Solved by Zeeshan Sarwar

variable_1 = 'Zeeshan'

"""
globals()
    Return the dictionary containing the current scope's global variables.

dir(...)
    dir([object]) -> list of strings
    
    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
"""

print("\n----------------------------------------------\n")
print("--------------------Checking with globals--------------------")

if 'variable_1' in globals():
    print(f"The variable {variable_1} is defined")
else:
    print(f"The variable {variable_1} is not defined")

print("\n----------------------------------------------\n")
print("--------------------Checking with dir--------------------")
if 'variable_1' in dir():
    print(f"The variable {variable_1} is defined")
else:
    print(f"The variable {variable_1} is not defined")
print("\n----------------------------------------------\n")

# print(help(dir))