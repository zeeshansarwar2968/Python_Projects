"""
3.  Write a Python program to get a string from a given string where all occurrences of its first char
    have been changed to '$', except the first char itself.
    Sample String : 'restart' Expected Result : 'resta$t'
"""
# Solved by Zeeshan Sarwar

sample_str = 'restart'
new_str = sample_str
index_list = [i for i in range(1, len(sample_str)) if sample_str.startswith(sample_str[0], i)]
print(f"Original string : {sample_str}")
for i in index_list: new_str = new_str[:5]+new_str[i:].replace(sample_str[i], '$')
print(f"Output string : {new_str}")

