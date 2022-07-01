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


def minor_matrix(matrix, i, j):
    """
    Returns caluclated minors of a matrix
    :param matrix: list of lists
    :param i: numeric value
    :param j: numeric value
    :return: list values
    """
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]


def determinant_matrix(matrix):
    """
    Returns a numberic value on calculation of determinant of  a matrix
    :param matrix: list of lists
    :return: numeric value
    """
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1)**c)*matrix[0][c]*determinant_matrix(minor_matrix(matrix, 0, c))
    return determinant


def inverse_matrix(matrix):
    """
    Returns  an inverse of a given matrix
    :param matrix: list of lists
    :return: list of lists
    """
    determinant = determinant_matrix(matrix)
    cofactors = []
    for r in range(len(matrix)):
        cofactorRow = []
        for c in range(len(matrix)):
            minor = minor_matrix(matrix, r, c)
            cofactorRow.append(((-1)**(r+c)) * determinant_matrix(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose_matrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


try:
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]
    for i in X: print(i)
    inv_matrix = inverse_matrix(X)
    print("The inverse of the above matrix is : \n")
    for i in inverse_matrix(X): print(i)
except Exception as e:
    print(f"Execution Interruption : {e}")






