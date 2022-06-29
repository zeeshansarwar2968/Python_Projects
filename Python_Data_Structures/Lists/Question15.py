"""
15. Write a Python program to find common items from two lists.
"""
# Solved by Zeeshan Sarwar

# sample list data
list_1 = [1, 2, 3, 4, 5, 343, 541, 12]
list_2 = [1, 2, 3, 4, 5, 343, 541, 671, 321]

set_1 = set(list_1)
set_2 = set(list_2)

print(f"Common items from two lists : {set_1 & set_2}")