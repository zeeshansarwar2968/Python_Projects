"""
35. Write a Python program to get numbers divisible by fifteen from a list using an anonymous
function.
"""
# Solved by Zeeshan Sarwar

try:
    count_numbers = int(input("Please provide the count of numbers to check : "))

    list_numbers = list()

    for i in range(count_numbers):
        temp = int(input("Element : "))
        list_numbers.append(temp)

    """
    filter(function or None, iterable) --> filter object
     |  
     |  Return an iterator yielding those items of iterable for which function(item)
     |  is true. If function is None, return the items that are true.
    """

    divisible_by_15_l = list(filter(lambda x: (x % 15 == 0), list_numbers))

    print(f"Numbers which are divisible by 15 are : {divisible_by_15_l}")

except ValueError:
    print("Please input numeric values")



# print(help(filter))