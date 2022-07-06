"""
3. Write a program to find the probability of drawing an ace after drawing an ace on the first draw
"""
# Solution by Zeeshan Sarwar

# Dependent events
# A pack of card contains 52 cards of 13pieces of 4 types of cards
# Out of 52 cards,one card can be drawn in 52 ways.

# There are 4 aces in a pack of 52 cards, out of which one ace can be drawn in 4 ways.

# Once an ace is drawn there are just three ace cards left
given_event = 3

sample_space = 51

try:
    print(f"The probability of drawing an ace from pack of cards is : {round(given_event/sample_space, 3)}")
except Exception as e:
    print(f"Error: {e}")