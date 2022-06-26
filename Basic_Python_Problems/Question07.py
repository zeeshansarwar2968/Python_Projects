"""
7. Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""
try:
    num_toCheck = int(input("Please provide the number to check : "))

    data_list = [1, 5, 8, 3]

    if num_toCheck in data_list:
        print(f"{num_toCheck} is present in {data_list} ")
    else:
        print(f"{num_toCheck} is not present in {data_list} ")

except ValueError:
    print("Please provide numeric value")



"""
Method 2:
print(num_toCheck in data_list)
"""

