"""
5. Write a program to find inverse matrix of matrix X in problem 1 .
"""
# Solution by Zeeshan Sarwar


def transpose_matrix(matrix):
    """
    Returns the transpose of a matrix
    :param matrix: list of lists
    :return: list of lists
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def minor_matrix(matrix):
    """
    Returns the minors of a matrix
    :param matrix: list of lists
    :return: list of lists
    """
    minors = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            temp = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]

            minors[i][j] = (temp[0][0] * temp[1][1]) - (temp[1][0] * temp[0][1])
    return minors


def cofactor_matrix(matrix):
    """
    Returns the cofactors of a matrix
    :param matrix: list of lists
    :return: list of lists
    """
    return [[matrix[i][j]*(-1)**(i+j) for j in range(len(matrix[0]))] for i in range(len(matrix))]


def determinant_matrix(matrix1, matrix2):
    """
    Returns the determinant of a matrix
    :param matrix1: list of lists
    :param matrix2: list of lists
    :return: numeric value
    """
    temp_values = map(lambda a, b: a * b, matrix1[0], matrix2[0])
    return sum(temp_values)


def inverseof_matrix(matrix, determinantvalue):
    """
    Returns the inverse of a matrix
    :param matrix: list of lists
    :param determinantvalue: numeric value
    :return: list of lists
    """
    return [[matrix[i][j]*(1/determinantvalue) for j in range(len(matrix[0]))] for i in range(len(matrix))]


X = [[3, 0, 2],
     [2, 0, -2],
     [0, 1, 1]]

X1 = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

try:
    # step 1 : calculating the Matrix of Minors
    minor_temp = minor_matrix(X1)
    # step 2 : turning the minor matrix into the Matrix of Cofactors
    cofactor_temp = cofactor_matrix(minor_temp)
    # step 3 : calculating the Adjugate(Adjoint) Matrix
    adjugate_temp = transpose_matrix(cofactor_temp)
    # step 4 : Calculating the determinant
    determinant = determinant_matrix(X1, cofactor_temp)
    # final step:: scalar multiplication of determinant and adjoint matrix
    inverse_matrix = inverseof_matrix(adjugate_temp, determinant)
    # printing the inverse matrix
    for i in inverse_matrix: print(i)
except Exception as e:
    print(f"Execution Interruption : {e}")






