# 2D Array
# a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
# standard input and printing them out to standard output.
# b. I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
# c. Logic -> create 2 dimensional array in memory to read in M rows and N cols
# d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter with
# OutputStreamWriter to print the output to the screen.

# Taking in user inputs for row and column definition
user_input1 = input("Please input the number of rows : ")
user_input2 = input("Please input the number of columns : ")

try:
    # explicit type casting of input value to integer
    row = int(user_input1)
    column = int(user_input2)

    matrix = []  # list to contain list elements for creation of a two dimensional array
    print("Enter the elements of row as below:")
    for i in range(row):
        temp = []   # creating a temporary array to append to the main matrix array
        for j in range(column):
            temp.append(int(input("Element : ")))   # appending elements taken from user to the temp list
        matrix.append(temp)

    print("The Two Dimensional array is printed below : ")
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end=" ")
        print()

except ValueError:
    print("Please input numeric values.")

