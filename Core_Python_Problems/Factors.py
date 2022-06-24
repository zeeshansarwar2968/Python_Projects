# Factors
# a. Desc -> Computes the prime factorization of N using brute force.
# b. I/P -> Number to find the prime factors
# c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency .
# d. O/P -> Print the prime factors of number N.
import math

user_input = input("Please provide a numeric value to print its prime factors : ")
try:
    N = int(user_input)
    while N % 2 == 0:  # initial run to find the count of 2 which are its factors
        print(2,)
        N = N/2
    for i in range(3, int(math.sqrt(N))+1):  # running a loop to find the factors after 2, using sqrt for efficiency
        while N % i == 0:
            print(i)
            N = N / i
    if N > 2:
        print(N)
except:
    print("Please provide a numeric value")
