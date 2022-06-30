"""
> 1. Write a python program to add below matrices
>     X = [[12,7,3], [4 ,5,6], [7 ,8,9]]
>     Y = [[5,8,1], [6,7,3], [4,5,9]]
"""
# Solution by Zeeshan Sarwar

# Matrix Addition
X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

Z = [[X[i][j] + Y[i][j] for j in range(len(X[i]))] for i in range(len(X))]

for i in Z: print(i)


# Long form method:

# for i in range(len(X)):
#     temp = []
#     for j in range(len(Y)):
#         temp.append(X[i][j] + Y[i][j])
#     Z.append(temp)
