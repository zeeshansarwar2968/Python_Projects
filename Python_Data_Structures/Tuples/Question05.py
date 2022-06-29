"""
5.  Write a Python program to find the repeated items of a tuple.
"""
# Solved by Zeeshan Sarwar

sample_tuple = ("Hello world", 432156, 432156, False, 34.6578, [1, 2, 43, 'Junction'], {23 : "Zeeshan", 24 : "Sarwar"})
print(f"The sample is :\n\t>>>> {sample_tuple}")
list1 = [x for x in sample_tuple if sample_tuple.count(x)>1]
print(f"\nThe repeated elements in the tuple are : {list1}")
