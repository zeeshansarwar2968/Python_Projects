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

user_input = input("Please input count of distinct Coupons: ")

try:
    couponNo = int(user_input)

    distinct = 0  # Total number of distinct coupons collected at a given stage
    count = 0  # Total number of coupons collected at a given stage

    # a list of size equal to couponNo(user input) with
    # initial false bool value for elements at each index
    isCollected = list()
    for i in range(couponNo):
        isCollected.append(False)

    # loop to check for unique coupon numbers at each iteration
    while distinct < couponNo:
        newCoupon = int(random.random() * couponNo)
        count += 1
        if not isCollected[newCoupon]:
            distinct += 1
            isCollected[newCoupon] = True

    print(f"Total random number needed to have all distinct coupons : {count}")

except ValueError:
    print("Please provide numeric input")












