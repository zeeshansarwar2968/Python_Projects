"""
23. Write a Python program to find the available built-in modules.
"""
"""
solved by : Zeeshan Sarwar
"""

import sys
import textwrap

# Method-1 --> use sys.builtin_module_names
built_in_modules_1 = ",".join(sys.builtin_module_names)
print(textwrap.fill(built_in_modules_1, width=80))
# print(textwrap.wrap(built_in_modules, width=80))

print("\n\n-----------------------------------------------------------------------------------------\n\n")

# Method-2 --> Use help to get all the modules available
# print(help('modules'))
built_in_modules_2 = ",".join(dir(__builtins__))
print(textwrap.fill(built_in_modules_2, width=80))