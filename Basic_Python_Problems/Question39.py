"""
39. Write a Python program to find files and skip directories of a given directory.
"""
# Solved by Zeeshan Sarwar

import os

dir_path = './'


"""
listdir(path=None)
    Return a list containing the names of the files in the directory.
    
    path can be specified as either str, bytes, or a path-like object.  If path is bytes,
      the filenames returned will also be bytes; in all other circumstances
      the filenames returned will be str.
    If path is None, uses the path='.'.
    On some platforms, path may also be specified as an open file descriptor;\
      the file descriptor must refer to a directory.
      If this functionality is unavailable, using it raises NotImplementedError.
"""
# print(help(os.listdir))
print(os.listdir(dir_path))
# print(os.path.join(dir_path, "Q"))
# print(help(os.path.join))
"""
join(path, *paths)
    # Join two (or more) paths.
"""
for value in os.listdir(dir_path):
   path = os.path.join(dir_path, value)
   if os.path.isdir(path):  # conditional block to skip directories
       continue
   print(value)