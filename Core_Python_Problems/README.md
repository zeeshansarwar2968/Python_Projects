# Basic Core Programs

1. User Input and Replace String Template “Hello <<UserName>>, How are you?”

a. I/P -> Take User Name as Input. Ensure UserName has min 3 char

b. Logic -> Replace <<UserName>> with the proper name

c. O/P -> Print the String with User Name


1. Flip Coin and print percentage of Heads and Tails

a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.

b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads

c. O/P -> Percentage of Head vs Tails


3. Leap Year

a. I/P -> Year, ensure it is a 4 digit number.

b. Logic -> Determine if it is a Leap Year.

c. O/P -> Print the year is a Leap Year or not.


4. Power of 2

a. Desc -> This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.

b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int

c. Logic -> repeat until i equals N.

d. O/P -> Print the year is a Leap Year or not.


5. Harmonic Number

a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
(http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).

b. I/P -> The Harmonic Value N. Ensure N != 0

c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N

d. O/P -> Print the Nth Harmonic Value.


6. Factors

a. Desc -> Computes the prime factorization of N using brute force.

b. I/P -> Number to find the prime factors

c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.

d. O/P -> Print the prime factors of number N.