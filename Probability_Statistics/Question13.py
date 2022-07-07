"""
> 13. The table below shows the height, x, in inches and the pulse rate, y, per minute,
> for 9 people. Write a program to find the correlation coefficient and interpret your result.
> x ⇒ 68 72 65 70 62 75 78 64 68
> y ⇒ 90 85 88 100 105 98 70 65 72
"""
# Solution by Zeeshan Sarwar

import math


def correlation_coeff(X, summation_X1X2, summation_X1, summation_X2, summation_X1_squared, summation_X2_squared):
    """
    Returns the z-value of the given input
    :param X: length of collection
    :param summation_X1X2: summation of all the multiplied values in collections X1 and X2
    :param summation_X1: summation of all values of collection X1
    :param summation_X2: summation of all values of collection X2
    :param summation_X1_squared: summation of all the squared values in collection X1
    :param summation_X2_squared: summation of all the squared values in collection X2
    :return: Calculate and return the correlation coefficient
    """
    return ((X * summation_X1X2) - (summation_X1 * summation_X2)) / (math.sqrt((X*summation_X1_squared-summation_X1**2)*(X*summation_X2_squared-summation_X2**2)))


# Given Values
x = [68, 72, 65, 70, 62, 75, 78, 64, 68]
y = [90, 85, 88, 100, 105, 98, 70, 65, 72]
N = 9

summation_xy = sum(map(lambda i,j:i*j , x, y))
summation_x = sum(x)
summation_y = sum(y)

value_x_square = [i*i for i in x]
value_y_square = [i*i for i in y]

summation_value_x_square = sum(value_x_square)
summation_value_y_square = sum(value_y_square)

try:
    print(f"\n-----------------------------------------------------------\n")
    correlation_coefficient = correlation_coeff(N, summation_xy, summation_x, summation_y, summation_value_x_square, summation_value_y_square)
    print(f"correlation_coefficient : {correlation_coefficient}")
    print(f"\n-----------------------------------------------------------\n")    
except Exception as e:
    print(f"Error: {e}")



# Old code
# correlation_coefficient = ((N * summation_xy) - (summation_x * summation_y)) / (math.sqrt((N*summation_value_x_square-summation_x**2)*(N*summation_value_y_square-summation_y**2)))
# print(f"correlation_coefficient : {correlation_coefficient}")