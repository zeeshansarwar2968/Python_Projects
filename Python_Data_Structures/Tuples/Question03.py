"""
3.  Write a Python program to unpack a tuple in several variables.
"""
# Solved by Zeeshan Sarwar

sample_tuple = ("Hello world", 432156, False, 34.6578, [1, 2, 43, 'Junction'], {23 : "Zeeshan", 24 : "Sarwar"})
print(f"The sample is :\n\t>>>> {sample_tuple}")

string_var, int_var, bool_var, float_var, list_var, dict_var = sample_tuple

print("\nThe unpacked variables are as follows : ")
print(f"string_var : {string_var}\nint_var : {int_var}\nbool_var : {bool_var}\nfloat_var : {float_var}\nlist_var : {list_var}\ndict_var : {dict_var}\n")