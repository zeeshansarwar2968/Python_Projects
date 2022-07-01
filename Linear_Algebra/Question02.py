"""
> 2. Write a program to perform scalar multiplication of matrix and a number
>     X = [[12,7,3], [4 ,5,6], [7 ,8,9]]
>     Y = 9
"""
# Solution by Zeeshan Sarwar


def scalar_mult(matrix, scaler):
     """
     return the scaler multiplication of a matrix
     :param matrix: list of lists
     :param scaler: numeric value
     :return: list of lists
     """
     return [[X[i][j] * 9 for j in range(len(X[i]))] for i in range(len(X))]

X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = 9

# Scaler Multiplication
try:
     Z = scalar_mult(X, Y)
     for i in Z: print(i)
except Exception as e:
     print(f"Execution interrupted due to {e}")




