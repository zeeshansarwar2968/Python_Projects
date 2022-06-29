"""
2. Write a Python program to count the number of characters (character frequency) in a string.
    Sample String : google.com
    Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
# Solved by Zeeshan Sarwar


sample_string = 'google.com'
str_list = list(sample_string)
dict_result = dict()
for i in str_list: dict_result[i] = dict_result.get(i, 0) + 1
print(f"The length of the input string data is : {dict_result}")