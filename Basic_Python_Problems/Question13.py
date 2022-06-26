"""
13. Write a Python program to find out the number of CPUs using.
"""
"""
solved by : Zeeshan Sarwar
"""
import os
import multiprocessing
import psutil
"""
os.cpu_count() method in Python is used to get the number of CPUs in the system. 
This method returns None if number of CPUs in the system is undetermined.

Syntax: os.cpu_count()

Parameter: No parameter is required.

Return Type: This method returns an integer value which denotes the number of CPUs in the system. 
None is returned if the number of CPUs is undetermined.
"""
print(os.cpu_count())

print(multiprocessing.cpu_count())
print(psutil.cpu_count())
print(psutil.cpu_count(logical = False))
print(psutil.Process().cpu_affinity())
print(os.sched_getaffinity(0))



# print(len(os.sched_getaffinity(0)))
# print(help(os))