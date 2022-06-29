"""
>   3. Write a Python script to concatenate following dictionaries to create a new one.
>       Sample Dictionary :
>       dic1={1:10, 2:20}
>       dic2={3:30, 4:40}
>       dic3={5:50,6:60}
"""
# Solved by Zeeshan Sarwar


dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
# We are using **kwargs to pass the dictionaries ans an argument to the new variable
dict4 = {**dict1, **dict2, **dict3}
print(dict4)