"""
5. Write a Python function that takes a list of words and returns the length of the longest one.
"""

str_list = ['hello', 'zeeshan', 'sarwar', 'machine', 'learning', 'artificial', 'intelligence']

len_list = [(len(i), i) for i in str_list]
len_list.sort()
print(f"The largest word in the list is : {len_list[-1][1]}")
