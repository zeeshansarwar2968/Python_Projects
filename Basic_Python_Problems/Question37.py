"""
37. Write a Python program to empty a variable without destroying it.
Sample data: n=20
d = {"x":200}
Expected Output : 0
{}
"""
# Solved by Zeeshan Sarwar

var_numeric = 432
var_dict = {'x': 432}
var_list = [1, 2, 3, 4, 5]
var_tuple = (1, 2, 3, 4, 5)

"""
type() returns the type of an object, which when called produces an 'empty' new value.

class type(object)
 |  type(object_or_name, bases, dict)
 |  type(object) -> the object's type
 |  type(name, bases, dict) -> a new type
When called, it accepts no arguments and returns a new featureless
 |      instance that has no instance attributes and cannot be given any.
"""

# print(help(type))


print("Empty Variable : ", type(var_numeric)())
print("Empty Variable : ", type(var_dict)())
print("Empty Variable : ", type(var_list)())
print("Empty Variable : ", type(var_tuple)())
