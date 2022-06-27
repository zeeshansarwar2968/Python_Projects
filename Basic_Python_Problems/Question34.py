"""
34. Write a Python program to retrieve file properties.
"""
# Solved by Zeeshan Sarwar

import os
import time

"""
ctime(seconds) -> string
Convert a time in seconds since the Epoch to a string in local time. This is equivalent to asctime(localtime(seconds)).
When the time tuple is not present, current time as returned by localtime() is used.

getsize(filename)
    Return the size of a file, reported by os.stat().
"""

print('File         :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modified time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))
# print(help(os.path.getsize))
print("\n------------------------\n")
################
"""
Perform a stat system call on the given path.
 
path
Path to be examined; can be string, bytes, a path-like object or open-file-descriptor int.
dir_fd
If not None, it should be a file descriptor open to a directory, and path should be a relative string; 
path will then be relative to that directory.
follow_symlinks
If False, and the last element of the path is a symbolic link, stat will examine the symbolic link 
itself instead of the file the link points to.
dir_fd and follow_symlinks may not be implemented
on your platform. If they are unavailable, using them will raise a NotImplementedError.
It's an error to use dir_fd or follow_symlinks when specifying path as
an open file descriptor.
"""

stats_file = os.stat("./")

print(stats_file)