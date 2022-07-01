"""
6. Write a program to find transpose matrix of matrix Y in problem 1
"""
# Solution by Zeeshan Sarwar


def transpose_matrix(matrix):
    """
    Returns the transpose of a matrix
    :param matrix: list of lists
    :return: list of lists
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

sample = [["a", "b", "c"],
          ["d", "e", "f"]]

sample1 = [['a', 'b'],
           ['c', 'd'],
           ['e', 'f']]

try:
    output = transpose_matrix(Y)
    print("--------------------")
    for i in output: print(i)
except Exception as e:
    print(f"Process Interrupted : {e}")

