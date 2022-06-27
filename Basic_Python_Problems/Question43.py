"""
43. Write a Python function to find the maximum and minimum numbers from a sequence of
numbers.
Note: Do not use built-in functions.
"""
# Solved by Zeeshan Sarwar

try:
    count_numbers = int(input("Please provide the count of numbers to check : "))

    list_numbers = list()

    for i in range(count_numbers):
        temp = int(input("Element : "))
        list_numbers.append(temp)
    """
    The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) 
    from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array. 
    """
    for i in range(count_numbers):
        indexer = i
        for j in range(i+1, count_numbers):
            if list_numbers[indexer] > list_numbers[j]:
                indexer = j
        list_numbers[i], list_numbers[indexer] = list_numbers[indexer], list_numbers[i]
    # list_numbers.sort()
    print(list_numbers)
    print(f"The largest number is : {list_numbers[-1]} \nThe smallest number is : {list_numbers[0]}")
except ValueError:
    print("Please Provide numeric input")
