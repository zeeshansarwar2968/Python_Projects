"""
11. Write a Python program to convert a list into a nested dictionary of keys.
"""
# Solved by Zeeshan Sarwar

num_list = [1, 2, 3, 4]
temp_dict = current = {}
for num in num_list:
    current[num] = {}
    current = current[num]
print(temp_dict)


# from functools import reduce
#
# li = ['a','b','c']
#
# d = reduce(lambda x, y: {y:x}, reversed(li+['']))
#
# print(d)
