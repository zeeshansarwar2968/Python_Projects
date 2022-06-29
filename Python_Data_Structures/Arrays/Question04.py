"""
4. Write a Python program to remove the first occurrence of a specified element from an
array.
"""
import array

print("Please Provide the elements of the array : ")
try:
    array_elements = array.array('i', [])
    for i in range(5): array_elements.append(int(input("Array Element : ")))

    to_find = int(input("Please input the number to remove : "))
    print("Original Array :", array_elements)
    index_element = array_elements.index(to_find)    # returning the index of the first occurrence of the element
    array_elements.pop(index_element)    # removing the element from the index from the array
    print("Modified Array :", array_elements)

except ValueError:
    print("Please Provide Numeric Inputs")