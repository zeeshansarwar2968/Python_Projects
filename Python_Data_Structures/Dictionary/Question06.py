"""
6. Write a Python program to remove a key from a dictionary.
"""

# Solved by Zeeshan Sarwar

user_inp = input("Please Provide size for the dictionary : ")
try:
    dict_size = int(user_inp)
    dict_count = {}
    for i in range(1,dict_size+1): dict_count[i] = i*i
    print(f"The original dictionary is : {dict_count}")
    print("-------------------------------\n")
    key_delete = int(input("PLease specify the key to delete value : "))
    dict_count.pop(key_delete)
    print(f"The modified dictionary is : {dict_count}")


except ValueError:
    print("Please Provide Numeric Inputs")