"""
4.  Write a Python program to create the colon of a tuple.
"""
# Solved by Zeeshan Sarwar

sample_tuple = ("Hello world", 432156, False, 34.6578, [1, 2, 43, 'Junction'], {23 : "Zeeshan", 24 : "Sarwar"})
print(f"The sample is :\n\t>>>> {sample_tuple}")
tuple_colon = sample_tuple[:]
tuple_colon[4].append("Hello")
print(f"\nThe colon of a tuple is :\n\t>>>> {tuple_colon}")
