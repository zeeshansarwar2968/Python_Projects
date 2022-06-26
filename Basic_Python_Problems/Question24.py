"""
24. Write a Python program to get the size of an object in bytes.
"""
"""
solved by : Zeeshan Sarwar
"""
import sys

obj_01 = "Hello World!!, My Name is Zeeshan Sarwar"

obj_02 = [x*x for x in range(20)]

"""
sys.getsizeof()
Return the size of an object in bytes. The object can be any type of object. 
All built-in objects will return correct results, but this does not have to hold true for 
third-party extensions as it is implementation specific
"""

print("Object 01 : ", obj_01)
print("Object 02 : ", obj_02)
print("\n---------------------------------------------------------------\n")
print(f"The size of object {obj_01} is : {sys.getsizeof(obj_01)} bytes")
print(f"The size of object {obj_02} is : {sys.getsizeof(obj_02)} bytes")