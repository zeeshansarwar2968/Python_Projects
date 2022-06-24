# Power of 2
# a. Desc -> This program takes a command-line argument N and prints a table of the
# powers of 2 that are less than or equal to 2^N.
# b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
# c. Logic -> repeat until i equals N.
# d. O/P -> Print the year is a Leap Year or not.

user_input = input("Please input a numeric value between 0 and 32 : ")
try:
    N = int(user_input)
    if 0<=N<31:
        for i in range(0,N+1):
            print(f"2^{i} : {2**i}")
    else: print("Please provide input in the given range")
except:
    print("Please input a numeric value")
