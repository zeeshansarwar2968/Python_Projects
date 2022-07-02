"""
> 3. Write a program to perform multiplication of given matrix and vector
>     X = [[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]], Y = [1, 2, 3]
"""
# Solution by Zeeshan Sarwar


def vector_mult(matrix, vector):
    """
    Return a vector as a result of multiplication of a matrix(nxn) with a vector(nx1)
    :param matrix: list of lists
    :param vector: a column-1 matrix(list)
    :return: a column-1 matrix(list)
    """
    temp = [[i[j] * vector[j] for j in range(len(i))] for i in matrix]
    return [sum(i) for i in temp]


# Matrix and vector multiplication
# The below program is valid for only nxn matrix and nx1 vector

X = [[5, 1, 3],     # 3x3
     [1, 1, 1],
     [1, 2, 1]]
Y = [1,             # 3x1
     2,
     3]

#
try:
    Z = vector_mult(X, Y)  # 3x1
    print(Z)
except Exception as e:
    print(f"Execution Interruption : {e}")


# Expanded logic
# for i in X:
#     temp = 0
#     for j in range(len(i)):
#         temp += i[j] * Y[j]
#     Z.append(temp)

# for i in Z: print(i)

# temp = [[i[j] * Y[j] for j in range(len(i))] for i in X]
# Z = [sum(i) for i in temp]  # 3x1
#########################################

