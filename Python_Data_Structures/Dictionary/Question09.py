"""
9. Write a Python program to print a dictionary in table format.
"""
# Solved by Zeeshan Sarwar

dict = {}
contact_dict = {
    'Contact1': ["John Doe 1", 31, 'India'],
    'Contact2': ["John Doe 2", 32, 'Korea'],
    'Contact3': ["John Doe 3", 33, 'Japan'],
    'Contact4': ["John Doe 4", 34, 'France'],
    'Contact5': ["John Doe 5", 35, 'Italy'],
         }

# Display column headers
print(f"\n{'Full Name':15} {'Age':10} {'Country':10} \n")

# piterate through each row of data and display them
for k, v in contact_dict.items():
    name, age, course = v
    print(f"{name:<15} {age:<10} {course:<10}")
