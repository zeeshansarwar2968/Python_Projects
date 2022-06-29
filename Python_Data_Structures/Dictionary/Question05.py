"""
5. Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""

# Solved by Zeeshan Sarwar

user_inp = input("Please Provide size for the dictionary : ")
try:
    dict_size = int(user_inp)
    dict_count = {}
    for i in range(1,dict_size+1): dict_count[i] = i*i
    print(f"The dictionary is : {dict_count}")
    print("-------------------------------\n")
    for i in dict_count: print(f"Key {i} : Value {dict_count[i]}")

except ValueError:
    print("Please Provide Numeric Inputs")