"""
40. Write a Python program to extract single key-value pair of a dictionary in variables.
"""
# Solved by Zeeshan Sarwar

temp_dict = {
    "value1" : 12345,
    "value2" : 67890,
    "value3" : "zeeshan",
    "value4" : "sarwar"
}

"""
items(...)
    D.items() -> a set-like object providing a view on D's items
"""
# print(help(dict.items))
for k,v in temp_dict.items():
    print("\n(k,v) pair values : ")
    print(f"key : {k}")
    print(f"Value : {v}")

