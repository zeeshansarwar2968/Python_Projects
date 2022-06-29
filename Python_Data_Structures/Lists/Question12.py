"""
12. Write a Python program to get the difference between the two lists.
"""
# Solved by Zeeshan Sarwar

# sample list data
list_1 = [1, 2, 3, 4, 5, 343, 541, 12]
list_2 = [1, 2, 3, 4, 5, 343, 541, 671, 321]

list_1_temp = set(list_1)
list_2_temp = set(list_2)

# temp_list = list_2+list_1
temp_set_1 = list_2_temp - list_1_temp
temp_set_2 = list_1_temp - list_2_temp

print(f"The the difference between the two lists are : {temp_set_1|temp_set_2}")