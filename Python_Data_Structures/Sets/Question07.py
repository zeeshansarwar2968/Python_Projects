"""
7. Write a Python program to create a union of sets.
"""
# Solved by Zeeshan Sarwar

print("The two sample sets for the program are : ")

set_1 = {32, 41, 45, 3, 97, 343, 144, 729, 512}
set_2 = {32, 41, 45, 3, 971, 343, 144, 629, 512, 1221, 16781}
print(f"First Sample set : {set_1} \nSecond Sample set : {set_2}")

# Union: contains all the elements of both the sets
print(f"\nThe union of set_1 and set_2 is : {set_1 | set_2}")
