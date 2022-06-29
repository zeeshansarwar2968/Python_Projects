"""
11. Write a Python program to generate all permutations of a list in Python.
"""
# Solved by Zeeshan Sarwar

import itertools

sample_list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

sample_list2 = ['a', 'b', 'c']

"""
class permutations(builtins.object)
 |  permutations(iterable, r=None)
 |  
 |  Return successive r-length permutations of elements in the iterable.
 |  
 |  permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)
"""
# print(help(itertools.permutations))
permutes = list(itertools.permutations(sample_list2))
print(f"All the {len(permutes)} permutations are as follows : ")
for i in permutes: print(i)
