"""
1. Write a program to find probability of drawing an ace from pack of cards
"""
# Solution by Zeeshan Sarwar


# A pack of card contains 52 cards of 13pieces of 4 types of cards
# Out of 52 cards,one card can be drawn in 52 ways.

# There are 4 aces in a pack of 52 cards, out of which one ace can be drawn in 4 ways.
given_event = 4
sample_space = 52

try:
    print(f"The probability of drawing an ace from pack of cards is : {round(given_event/sample_space, 3)}")
except Exception as e:
    print(f"Error : {e}")