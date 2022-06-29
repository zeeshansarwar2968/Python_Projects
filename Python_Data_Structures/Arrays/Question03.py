"""
3. Write a Python program to get the number of occurrences of a specified element in an
array.
"""
# Solved by Zeeshan Sarwar

import array

print("Please Provide the elements of the array : ")
try:
    dict_count = {}
    array_elements = array.array('i',[])
    for i in range(5): array_elements.append(int(input("Array Element : ")))
    to_find = int(input("Please input the number to get number of occurrences : "))
    for i in array_elements: dict_count[i] = dict_count.get(i, 0)+1

    print(f"The element {to_find} has {dict_count[to_find]} occurrences")
except ValueError:
    print("Please Provide Numeric Inputs")
