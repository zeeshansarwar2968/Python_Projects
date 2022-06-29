"""
13. Write a Python program to count number of items in a dictionary value that is a list.
"""

dict_data = {'Name_List1': ['subj1', 'subj2', 'subj3'],
             'Name_List2': ['subj1', 'subj2'],
             'Name1': ['subj1'],
             'Name_List3': ['subj1', 'subj2', 'subj3', 'subj4'],
             'Name_List4': ['subj1', 'subj2', 'subj3'],
             }
"""
class map(object)
 |  map(func, *iterables) --> map object
 |  
 |  Make an iterator that computes the function using arguments from
 |  each of the iterables.  Stops when the shortest iterable is exhausted.
 """

print(dict_data.values())
total_counter = sum(map(len, dict_data.values()))
print(total_counter)
print(map(len, dict_data.values()))
# print(help(map))