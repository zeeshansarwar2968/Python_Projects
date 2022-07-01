"""
4. Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""
# Solved by Zeeshan Sarwar


sample_list = ['abc', 'xyz', 'aba', '1221', 'q', 'p']
final_list = [x for x in sample_list if len(x) >= 2 and x[0] == x[-1]]
print(f"The count of strings : {len(final_list)}")

