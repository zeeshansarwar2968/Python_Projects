# Harmonic Number
# a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
# (http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
# b. I/P -> The Harmonic Value N. Ensure N != 0
# c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
# d. O/P -> Print the Nth Harmonic Value.

user_input = input("Please input a numeric value : ")
harmonic_number = 0
try:
    N = int(user_input)
    if N != 0:
        for i in range(1, N+1):
            harmonic_number = harmonic_number + (1/i)
    else: print("Please provide a non-zero input")
    print(f"The Nth Harmonic Number for {N} is : {harmonic_number}")
except:
    print("Please provide a numeric value")


