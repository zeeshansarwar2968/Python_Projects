"""
41. Write a Python program to convert an integer to binary keep leading zeros.
Sample data : 50
Expected output : 00001100, 0000001100
"""
# Solved by Zeeshan Sarwar

input_int = int(input("Please provide the integer number to convert to binary : "))

"""
bin(number, /)
    Return the binary representation of an integer.
    
    >>> bin(2796202)
    '0b1010101010101010101010'
"""
print("\n-------------------------------------------------------")
print("Calculating Binary value using the bin method----------")
# print(help(bin))
print(bin(input_int).replace("0b", ""))
print(bin(input_int)[2:])

"""
format(value, format_spec='', /)
    Return value.__format__(format_spec)
    
    format_spec defaults to the empty string.
    See the Format Specification Mini-Language section of help('FORMATTING') for
    details.

"""
print("\n----------------------------------------------------------")
print("Calculating Binary value using the format method----------")
# print(help(format))
print(format(input_int, '08b'))
print(format(input_int, '010b'))