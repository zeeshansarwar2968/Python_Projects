"""
26. Write a Python program to count the number occurrence of a specific character in a string.
"""
"""
solved by : Zeeshan Sarwar
"""
str = "This is awesome and amazing"
str_list = list("".join(str.split()))

str_dict = {}

for i in str_list:
    str_dict[i] = str_dict.get(i, 0)+1


# for k,v in str_dict.items():

list_tuple = [(v, k) for k, v in str_dict.items()]
list_tuple.sort(reverse=True)

for i in list_tuple:
    print(f"{i[1]} : {i[0]}")