"""
 4. Write a program to multiply matrices in problem 1
"""
# Solution by Zeeshan Sarwar


def matrix_mult(matrix1, matrix2):
    """
    Returns a matrix of teh product of matrrix1 and matrix2
    :param matrix1: list of lists (mxn)
    :param matrix2: list of lists (mxn)
    :return: list of lists (mxn)
    """
    temp = [[0 for i in range(len(matrix2[0]))] for i in range(len(matrix1))]
    for i in range(len(matrix1)):  # looping over the rows of matrix A
        for j in range(len(matrix2[0])):  # looping over the columns of matrix B
            for k in range(len(matrix2)):  # looping over the rows of matrix B
                temp[i][j] += matrix1[i][k] * matrix2[k][j]
    return temp


# Matrix Multiplication
X = [[12, 7, 3],  # mxm
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 8, 1],  # mxm
     [6, 7, 3],
     [4, 5, 9]]

try:
    Z = matrix_mult(X, Y)
    for i in Z: print(i)
except Exception as e:
    print(f"Execution Interrupted : {e}")


