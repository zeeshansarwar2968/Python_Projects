"""
10. Write a Python program to count occurrences of a substring in a string.
"""
# Solved by Zeeshan Sarwar

sample_str = 'lorem ipsum dolor sit amet, ipsum lorem adipiscing lorem ipsum elit'
sub_str = 'lorem'
new_str = sample_str
index_list = [i for i in range(len(sample_str)) if sample_str.startswith(sub_str, i)]
print(f"\nOriginal string : {sample_str}")
print(f"Count of occurrences of substring '{sub_str}' in the string : {len(index_list)}")


# Logic No.2 Easier
print("\n")
count = sample_str.count(sub_str)
print(f'Method :: 02 \nCount of occurrences : {count}')