"""
8. Write a Python program to create set difference.
"""
# Solved by Zeeshan Sarwar

print("The two sample sets for the program are : ")

set_1 = {32, 41, 45, 3, 97, 343, 144, 729, 512}
set_2 = {32, 41, 45, 3, 971, 343, 144, 629, 512, 1221, 16781}
print(f"First Sample set : {set_1} \nSecond Sample set : {set_2}")

# difference() : returns a set that is the difference between two sets.

# set_1 - set_2 is equal to the elements present in set_1 but not in set_2
print(f"\nThe difference set_1 - set_2 is : {set_1 - set_2}")
# set_2 - set_1 is equal to the elements present in set_2 but not in set_1
print(f"\nThe difference set_2 - set_1 is : {set_2 - set_1}")