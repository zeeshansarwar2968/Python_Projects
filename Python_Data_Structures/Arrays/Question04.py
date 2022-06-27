"""
4. Write a Python program to remove the first occurrence of a specified element from an
array.
"""

print("Please Provide the elements of the array : ")
try:
    dict_count = {}
    list_elements = [int(input("Element : ")) for i in range(5)]

    to_find = int(input("Please input the number to remove : "))

    index_element = list_elements.index(to_find)    # returning the index of the first occurrence of the element
    list_elements.pop(index_element)    # removing the element from the index from the list
    print(list_elements)

except ValueError:
    print("Please Provide Numeric Inputs")