"""
1. Write a Python script to sort (ascending and descending) a dictionary by
value.
"""
# Solved by Zeeshan Sarwar

print("Please Provide values for the dictionary : ")
try:
    dict_count = {}
    for i in range(6): dict_count[i+1] = int(input("Value : "))
    print(f"The original dictionary is : {dict_count}")
    list_ascending = [(v, k) for k, v in dict_count.items()]
    list_ascending.sort()
    print(f"The dictionary sorted in ascending order by value : {list_ascending}")
    list_descending = [(v, k) for k, v in dict_count.items()]
    list_descending.sort(reverse=True)
    print(f"The dictionary sorted in descending order by value : {list_descending}")

except ValueError:
    print("Please Provide Numeric Inputs")
