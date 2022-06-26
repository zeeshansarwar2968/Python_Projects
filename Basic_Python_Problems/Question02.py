"""
2. Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""
"""
solved by : Zeeshan Sarwar
"""

user_input = input("Please specify the size of the data sequence : ")

data_size = int(user_input)

list_output = list()

print("Please input the elements for the data sequence : ")
for i in range(data_size):
    temp_input = input("Element of the list : ")
    list_output.append(temp_input)

print(f"The list is : {list_output} and ,\n the tuple is : {tuple(list_output)}")
