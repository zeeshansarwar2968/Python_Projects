"""
20. Write a Python program to sort three integers without using conditional statements and
loops.
"""

"""
solved by : Zeeshan Sarwar
"""


print("Please provide the three numbers to sort : ")
try:
    list_numbers = []

    for i in range(3):
        temp_input = int(input("Element of the list : "))
        list_numbers.append(temp_input)

    print(f"The input is : {list_numbers}")
    list_numbers.sort()
    print(f"The ordered list is : {list_numbers}")

except ValueError:
    print("Please provide only numeric values")




