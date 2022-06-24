# Factors
# a. Desc -> Computes the prime factorization of N using brute force.
# b. I/P -> Number to find the prime factors
# c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency .
# d. O/P -> Print the prime factors of number N.

import math  # importing math lib to use the inbuilt sqrt method

user_input = input("Please provide a numeric value to print its prime factors : ")
try:
    N = int(user_input)  # explicit type casting of input value to integer
    # running a loop to determine the count of 2 which are a factor of num and printing them
    while N % 2 == 0:
        print(2,)
        N = N/2     # dividing the number by 2 and storing the value in each true iteration

    # second loop to find the remaining prime factors by looping till the square root of N
    for i in range(3, int(math.sqrt(N))+1):  # using sqrt for efficiency, while maintaining functionality
        while N % i == 0:
            print(i)
            N = N / i

    # last conditional statement to print the remaining N value if greater than 2
    if N > 2:
        print(N)
except ValueError:
    print("Please provide a numeric value")
