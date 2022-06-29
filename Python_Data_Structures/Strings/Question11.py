"""
11. Write a Python program to reverse a string.
"""

def rev_str(stringdata):
    """
    Return a reversed string
    :param stringdata: string
    :return: string
    """
    tempdata = list(stringdata)
    tempdata.reverse()
    return "".join(tempdata)


sample_str = 'zeeshan'
print(f"The original string is : {sample_str}")
rev_string = rev_str(sample_str)
print(f"The reversed string is : {rev_string}")
