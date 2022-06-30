"""
> 3. Write a program to perform multiplication of given matrix and vector
>     X = [[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]], Y = [1, 2, 3]
"""
# Solution by Zeeshan Sarwar

# Matrix and vector multiplication
# The below program is valid for only nxn matrix and nx1 vector

X = [[5, 1, 3],     # 3x3
     [1, 1, 1],
     [1, 2, 1]]
Y = [1,             # 3x1
     2,
     3]

temp = [[i[j] * Y[j] for j in range(len(i))] for i in X]
Z = [sum(i) for i in temp]  # 3x1
print(Z)

# Expanded logic
# for i in X:
#     temp = 0
#     for j in range(len(i)):
#         temp += i[j] * Y[j]
#     Z.append(temp)

# for i in Z: print(i)

