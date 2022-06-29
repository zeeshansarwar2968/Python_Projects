"""
9. Write a Python function that takes two lists and returns True if they have at
least one common member.
"""
# Solved by Zeeshan Sarwar

# sample list data
list_1 = [1, 2, 3, 4, 5, 343, 541]
list_2 = [1, 2, 3, 4, 5, 343, 541, 671, 321]
# temp list and set
temp_list = list_2.copy()
temp_list.extend(list_1)
temp_set = set(temp_list)
validity = False if len(temp_set) == len(list_1)+len(list_2) else True
print(validity)
