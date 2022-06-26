"""
2. Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
"""
Solution 2
solved by : Zeeshan Sarwar
"""

user_input = input("Please specify the size of the data sequence : ")

data_size = int(user_input)

list_input = ""

print("Please input the elements for the data sequence : ")

for i in range(data_size-1):
    temp_input = input("Element of the list : ")
    list_input += temp_input
    list_input += ","
temp_input = input("Element of the list : ")
list_input += temp_input
print(f"The input is : {list_input}")

list_output = list_input.split(",")
tuple_output = tuple(list_output)
print(f"The list is : {list_output} and,\nThe tuple is : {tuple_output}")