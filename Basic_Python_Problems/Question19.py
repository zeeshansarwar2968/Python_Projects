"""
19. Write a Python program to get file creation and modification date/times.
"""
"""
solved by : Zeeshan Sarwar
"""

import os
"""
os.path.getmtime(path): Cross-platform way to get file modification time in Python. 
It returns the Unix timestamp of when the file was last modified.

os.path.getctime('file_path'): To get file creation time on windows.
"""

path_value = "C:/Users/zeesh/Desktop/CFP/Python/Python_Projects/Basic_Python_Problems/Question16.py"

print(f"The file creation time is : {os.path.getctime(path_value)}")
print(f"The file modification time is : {os.path.getmtime(path_value)}")
