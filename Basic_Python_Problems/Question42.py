"""
42. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode
on operating system.
"""
# Solved by Zeeshan Sarwar

import platform
# platform.system()
"""
architecture(executable='C:\\Users\\zeesh\\anaconda3\\python.exe', bits='', linkage='')
    Queries the given executable (defaults to the Python interpreter
    binary) for various architecture information.
    
    Returns a tuple (bits, linkage) which contains information about
    the bit architecture and the linkage format used for the
    executable. Both values are returned as strings.
"""

print(platform.architecture()[0])
print(platform.architecture())
# print(help(platform.architecture))
print(platform.machine())
print(platform.platform())
print(platform.processor())
print(platform.release())
