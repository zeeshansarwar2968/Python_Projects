"""
25. Write a Python program to get the current value of the recursion limit.
"""
"""
solved by : Zeeshan Sarwar
"""

import sys
"""
getrecursionlimit()
    Return the current value of the recursion limit.
    
    The recursion limit is the maximum depth of the Python interpreter
    stack.  This limit prevents infinite recursion from causing an overflow
    of the C stack and crashing Python.
"""
print(f"The current value of the recursion limit is : {sys.getrecursionlimit()}")
print(help(sys.getrecursionlimit))