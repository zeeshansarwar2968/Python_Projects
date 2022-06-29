"""
4. Write a Python program to iterate over dictionaries using for loops.
"""

# Solved by Zeeshan Sarwar

print("Please Provide values for the dictionary : ")
try:
    dict_count = {}
    for i in range(6): dict_count[i+1] = int(input("Value : "))
    print(f"The original dictionary is : {dict_count}")
    print("-------------------------------\n")
    for i in dict_count: print(f"Key {i} : Value {dict_count[i]}")

except ValueError:
    print("Please Provide Numeric Inputs")