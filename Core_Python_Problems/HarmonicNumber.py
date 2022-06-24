# Harmonic Number
# a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
# (http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
# b. I/P -> The Harmonic Value N. Ensure N != 0
# c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
# d. O/P -> Print the Nth Harmonic Value.

# taking in user input to calculate harmonic number
user_input = input("Please input a numeric value : ")
harmonic_number = 0     # initialising a variable to store the harmonic number and the subsequent addition in series

try:
    N = int(user_input)     # explicit type casting of input value to integer

    if N != 0:      # conditional check for a non zero input
        for i in range(1, N+1):
            harmonic_number = harmonic_number + (1/i)      # adding the subsequent value in each iteration to variable
    else:
        print("Please provide a non-zero input")

    print(f"The Nth Harmonic Number for {N} is : {harmonic_number}")

except ValueError:      # using except block to catch value based errors during the input stage
    print("Please provide a numeric value")


