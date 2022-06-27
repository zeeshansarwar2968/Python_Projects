"""
31. Write a Python program to get system command output.
"""
# Solved by Zeeshan Sarwar

import subprocess

"""
run(*popenargs, input=None, capture_output=False, timeout=None, check=False, **kwargs)
    Run command with arguments and return a CompletedProcess instance.
"""
print(help(subprocess.run))
print("Listing all the files and directories using the dir command : ")
data = subprocess.run("dir", shell=True, universal_newlines=True)


