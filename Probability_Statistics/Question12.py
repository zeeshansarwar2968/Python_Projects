"""
12. Write a program to find the probability of getting a random number from the interval [2, 7]
"""
# Solution by Zeeshan Sarwar

import random

interval = list(range(2,7+1))

try:
    probability_random_number = 1/len(interval)
    print(f"Probability of getting a random number from the interval [2, 7] is : {round(probability_random_number, 3)}")
except Exception as e:
    print(f"Error: {e}")