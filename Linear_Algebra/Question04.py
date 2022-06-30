"""
 4. Write a program to multiply matrices in problem 1
"""
# Solution by Zeeshan Sarwar

# Matrix Multiplication
X = [[12, 7, 3],  # mxm
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 8, 1],  # mxm
     [6, 7, 3],
     [4, 5, 9]]

Z = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # mxm

for i in range(len(X)):  # looping over the rows of matrix A
    for j in range(len(Y[0])):  # looping over the columns of matrix B
        for k in range(len(Y)):  # looping over the rows of matrix B
            Z[i][j] += X[i][k] * Y[k][j]

for i in Z: print(i)
