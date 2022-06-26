"""
8. Write a Python program to create a histogram from a given list of integers.
"""

size_list = int(input("Please define the size of array : "))

histogram = {}

list_data = []

print("Please provide the list of integers to generate a histogram : ")

for i in range(size_list):
    temp = int(input("Element : "))
    list_data.append(temp)

for i in list_data:
    histogram[i] = histogram.get(i, 0) + 1

for i in histogram:
    print(f"{i} : {histogram[i]}")
