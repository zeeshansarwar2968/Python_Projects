"""
8.  Write a Python program to get the last part of a string before a specified character.
"""
# Solved by Zeeshan Sarwar


string_data = input("Please input the string: ")
specified_char = input("Please input the specified character : ")

print(f"The last part of the string before a specified character : {string_data.split(specified_char, 1)[0]}")
print(f"\nThe last character before a specified character : {string_data.split(specified_char, 1)[0][-1]}")

