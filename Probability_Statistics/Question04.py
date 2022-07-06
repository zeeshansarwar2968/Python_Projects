"""
> 4. You toss a fair coin three times write a program to find following:
> a. What is the probability of three heads, HHH?
> b. What is the probability that you observe exactly one heads?
> c. Given that you have observed at least one heads, what is the probability that you observe at least two heads?
"""
# Solution by Zeeshan Sarwar

import itertools

# When a coin is tossed three times the sample space is 2**3 = 8 i.e., possible outcomes multiplied by the total experiment count
sample_space = ['HHH', 'HTH', 'HTT', "HHT", 'TTT', 'THT', 'THH', 'TTH']

# Filtering the elements with just one H
# space_oneH = [x[i] for i in range(len(sample_space)) if x[i].count('H') == 1 ]
space_oneH = list(filter(lambda x: x.count('H') == 1, sample_space))

try:
    print('one H :',space_oneH)
    print(f"The probability of getting three heads (HHH) is : {sample_space.count('HHH')/len(sample_space)}")
    print(f"The probability of observing exactly one head is : {len(space_oneH)/len(sample_space)}")
    print(f"The probability of observing at least two head is : {(len(space_oneH)/len(sample_space))*((len(space_oneH)-1)/(len(sample_space)-1))}")
except Exception as e:
    print(f"Error: {e}")


