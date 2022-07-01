"""
> 1. Write a python program to add below matrices
>     X = [[12,7,3], [4 ,5,6], [7 ,8,9]]
>     Y = [[5,8,1], [6,7,3], [4,5,9]]
"""
# Solution by Zeeshan Sarwar


def matrix_addition(matrix1, matrix2):
     """
     Returns a matrix of same order as the input with summed values
     :param matrix1: array of arrays
     :param matrix2: array of arrays
     :return: array of arrays
     """
     return [[X[i][j] + Y[i][j] for j in range(len(X[i]))] for i in range(len(X))] if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]) else "" "The matrices are not of same order"


# Matrix Addition
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
try:
     Z = matrix_addition(X, Y)
     for i in Z: print(i)
except Exception as e:
     print(f"Execution Interrupted : {e}")




# Long form method:

# for i in range(len(X)):
#     temp = []
#     for j in range(len(Y)):
#         temp.append(X[i][j] + Y[i][j])
#     Z.append(temp)

# def matrix_additon(matrix1, matrix2):
#      """
#      Returns a matrix of same order as input with added values
#      :param matrix1: array of arrays
#      :param matrix2: array of arrays
#      :return: array of arrays
#      """
#      if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
#           return [[X[i][j] + Y[i][j] for j in range(len(X[i]))] for i in range(len(X))]
#      else: return "The matrices are not of same order"