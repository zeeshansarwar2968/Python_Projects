"""
8. Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
"""
# Solved by Zeeshan Sarwar

sample_str = 'w3resource'
sample_list = list(sample_str)
sample_dict = {}
for i in sample_list: sample_dict[i] = sample_dict.get(i, 0)+1
print(f"Sample string : {sample_str}")
print(f"Expected output : {sample_dict}")
