"""
17. Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
"""
# Solved by Zeeshan Sarwar

# Method 1
sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

temp_tuples = [tuple(i) for i in sample_list]
temp_dict = {}
for i in temp_tuples: temp_dict[i] = temp_dict.get(i, 0)+1
print(temp_dict)
final_list = list(temp_dict.keys())
final = [list(i) for i in final_list]
print(final)

# Method 2
print("--------------------------\n")
import itertools
sample_list.sort()
print(list(i for i,_ in itertools.groupby(sample_list)))