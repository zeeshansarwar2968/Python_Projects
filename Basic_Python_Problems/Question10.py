"""
10. Write a Python program to print out a set containing all the colors from color_list_1 which are
not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""
"""
solved by : Zeeshan Sarwar
"""
color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]
color_set_1 = set(color_list_1)
color_set_2 = set(color_list_2)

# set.difference returns a set that contains the items that only exist in set x, and not in set y
unique_set = color_set_1.difference(color_set_2)

print(f"All the colors from color_list_1 which are not present in color_list_2 are : {unique_set}")

