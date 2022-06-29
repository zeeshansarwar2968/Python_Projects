"""
2. Write a Python script to add a key to a dictionary.
>       Sample Dictionary : {0: 10, 1: 20}
>       Expected Result : {0: 10, 1: 20, 2: 30}
"""
# Solved by Zeeshan Sarwar

dict_existing = {0: 10, 1: 20}

try:
    dict_key = int(input("Please provide the numeric key data for the dictionary : "))
    dict_value = int(input("Please provide the numeric value data for the dictionary : "))
    print(f"The original dictionary is : {dict_existing}")

    dict_existing[dict_key] = dict_value
    print(f"The updated dictionary is : {dict_existing}")

except ValueError:
    print("Please input numeric values only")
