# Flip Coin and print percentage of Heads and Tails
# a. I/P -> The number of times to Flip Coin. Ensure it is positive integer .
# b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
# heads
# c. O/P -> Percentage of Head vs Tails

import random  # importing random module to randomise the coin flip process

# Taking in input from the user to control the iteration count
user_input = input("Please enter the number of times to flip the coin : ")

try:
    flips = int(user_input)
    headCounter = 0
    tailCounter = 0
    tempCounter = flips

    if flips > 0:
        while tempCounter > 0:      # Starting an indefinite loop to iterate through the flip count provided by user
            randomValue = random.randint(0, 1)      # using random module to randomize the flipping process
            if randomValue == 0:
                tailCounter = tailCounter + 1       # incrementing heads/tails count on the basis of the random value
            else:
                headCounter = headCounter + 1
            tempCounter = tempCounter - 1

    # Calculating the head and tail occurrence percentage
    headPercentage = (headCounter / (headCounter + tailCounter)) * 100
    tailPercentage = (tailCounter / (headCounter + tailCounter)) * 100
    # printing out the final percentage anf count for both the heads and tails
    print(f"The percentage of heads is : {headPercentage}% and the count of heads is {headCounter}")
    print(f"The percentage of tails is : {tailPercentage}% and the count of tails is {tailCounter}")

except ValueError:      # Except block to catch any valueError thrown during runtime
    print("Please provide a valid integer input")
except ZeroDivisionError:       # Except block to catch any ZeroDivisionError thrown during runtime
    print("Please provide a positive integer input")


