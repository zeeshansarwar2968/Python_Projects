# 2D Array
# a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
# standard input and printing them out to standard output.
# b. I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
# c. Logic -> create 2 dimensional array in memory to read in M rows and N cols
# d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter with
# OutputStreamWriter to print the output to the screen.


user_input1 = input("Please input the number of rows : ")
user_input2 = input("Please input the number of columns : ")

row = int(user_input1)
column = int(user_input2)

matrix = []   # list to contain list elements for creation of a two dimensional array
print("Enter the elements of row as below:")
for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)

print("The 2D array is given below:")
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")
    print()