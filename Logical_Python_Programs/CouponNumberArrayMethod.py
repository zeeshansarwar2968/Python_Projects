# Coupon Numbers
# a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
# need to generate distinct coupon number? This program simulates this random
# process.
# b. I/P -> N Distinct Coupon Number
# c. Logic -> repeatedly choose a random number and check whether it's a new one.
# d. O/P -> total random number needed to have all distinct numbers.
# e. Functions => Write Class Static Functions to generate random number and to
# process distinct coupons.

import random   # importing random module to generate random values
# importing array module to use arrays as we want a contiguous type safe data structure
from array import array     # We also want to perform operations directly on the array

user_input = input("Please input count of distinct Coupons: ")


def is_collected(value, n):
    """
    This function returns a value of 1 or 0 on condition check
    :param value: in context of current project, this takes in the randomly generated value
    :param n: in context of current project, this takes in the user provided coupon count
    :return: 0 or 1
    """
    if value <= n:
        return 1
    else:
        return 0

try:
    N = int(user_input)
    x = array('i', [1, 0])  # Array of coupon
    count = 0  # Total number of coupons collected at a given stage
    distinct = 0  # Total number of distinct coupons collected at a given stage

    # repeatedly choose a random value/coupon and check whether it's a new one
    while distinct < N:
        random_value = int((random.randint(0, N)) * N - 1)  # random value between 0 and n-1
        # print("Random Number Generated : ", value)
        count = count + 1  # we collected one more coupon and increment the counter
        # print("Count of each random Number : ", count)
        res = is_collected(random_value, N)
        y = x[res]
        # print(y)
        if not y:
            distinct = distinct + 1
            # isCollected = True
        # print(f"The total number of coupons generated are : {count}")
    print(f"The total number of coupons generated are : {count}")
except ValueError:
    print("Please provide a numeric value")






