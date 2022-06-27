"""
Cross Game or Tic-Tac-Toe Game
a. Desc -> Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1 is
the Computer and the Player 2 is the user. Player 1 take Random Cell that is the
Column and Row.
b. I/P -> Take User Input for the Cell i.e. Col and Row to Mark the ‘X’
c. Logic -> The User or the Computer can only take the unoccupied cell. The Game
is played till either wins or till draw...
d. O/P -> Print the Col and the Cell after every step.
e. Hint -> The Hints is provided in the Logic. Use Functions for the Logic…
"""


# user_input1 = input("Rows : ")
# user_input2 = input("Columns : ")


import random

board = [i for i in range(0, 9)]
player, computer = '', ''

# Corners, Center and Others, respectively
moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))

# Winner combinations
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

# Table
tab = range(1, 10)



