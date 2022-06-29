"""
12. Write a Python program to check multiple keys exists in a dictionary.
"""

# Solved by Zeeshan Sarwar

def key_check(dictvalue, keyvalue):
    """
    Returns boolean if specified keys exist in dictionary
    :param dictvalue: dictionary
    :param keyvalue: key values
    :return: boolean
    """
    return dictvalue.keys() >= keyvalue

sample_dict = {'id': 1, 'success': True, 'name': 'Lary'}

print(key_check(sample_dict, {'id', 'success', 'name'}))
# print(sample_dict.keys() <= {'id', 'name'})
# print(type(sample_dict.keys()))
print(key_check(sample_dict, {'id', 'name'}))
print(key_check(sample_dict, {'id', 'name1'}))

