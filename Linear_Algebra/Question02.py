"""
> 2. Write a program to perform scalar multiplication of matrix and a number
>     X = [[12,7,3], [4 ,5,6], [7 ,8,9]]
>     Y = 9
"""
# Solution by Zeeshan Sarwar

# Scaler Multiplication

X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
Y = 9

Z = [[X[i][j] * 9 for j in range(len(X[i]))] for i in range(len(X))]

for i in Z: print(i)
