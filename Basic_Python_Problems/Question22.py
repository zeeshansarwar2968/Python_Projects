"""
22. Write a Python program to get the command-line arguments (name of the script, the number
of arguments, arguments) passed to a script.
"""
"""
solved by : Zeeshan Sarwar
"""
import sys

# print(f"arguments : {sys.argv}")
# print(f"Number of arguments: {len(sys.argv)} arguments.")
# print(f"Argument List: {str(sys.argv)}")

arg_count = len(sys.argv)
print(f"Total arguments passed : {arg_count}")

print(f"Name of the python script/file : {sys.argv[0]}")

# Printing the arguments :
for i in range(1, arg_count):
    print(f"Argument {i} : {sys.argv[i]}")

temp_sum = 0

for i in range(1, arg_count):
    temp_sum += int(sys.argv[i])

print(f"The temporary summation is : {temp_sum}")

