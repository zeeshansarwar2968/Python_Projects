"""
7. Write a Python program that accepts a comma separated sequence of words as input and prints
   the unique words in sorted form (alphanumerically).
    Sample Words : red, white, black, red, green, black
    Expected Result : black, green, red, white,red
"""
# Solved by Zeeshan Sarwar

# str_input = ['red', 'white', 'black', 'red', 'green', 'black']
str_input = "red, white, black, red, green, black"
temp_list = str_input.split(",")
str_list = [i.strip() for i in temp_list]
str_set = set(str_list)
str_list = list(str_set)
str_list.sort()
print(f"The sorted word list is : {str_list}")
