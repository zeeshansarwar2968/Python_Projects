"""
32. Write a Python program to get the effective group id, effective user id, real group id, a list of
supplemental group ids associated with the current process.
Note: Availability: Unix.
"""
# Solved by Zeeshan Sarwar

import os
print("Python program to get the effective group id, effective user id, real group id, a list of \n "
      "supplemental group ids associated with the current process")
print("\n-------------------------------------------------\n")
print(f"The effective group id of the current process is : {os.getegid()}")
print(f"The effective user id of the current process is : {os.geteuid()}")
print(f"The real group id of the current process is : {os.getgid()}")
print(f"List of supplemental group ids: {os.getgroups()}")
print("\n-------------------------------------------------\n")