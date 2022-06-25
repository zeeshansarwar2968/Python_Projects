# Gambler
# a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
# he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
# times he/she wins and the number of bets he/she makes. Run the experiment N
# times, averages the results, and prints them out.
# b. I/P -> $Stake, $Goal
# c. Logic -> Play till the gambler is broke or has won
# d. O/P -> Print Number of Wins and Percentage of Win and Loss.

import random  # importing random module to randomise each gamble

# Taking in input parameters from the user
user_input1 = input("Please input the stake amount : ")
user_input2 = input("Please input the Goal amount : ")
user_input3 = input("Please input the experiment Count : ")

try:
    # explicit type casting of input value to integer
    stake = int(user_input1)
    goal = int(user_input2)
    bet_count = int(user_input3)

    # Conditional run of the program if goal amount is bigger than stake
    if stake < goal:
        winCounter = 0
        lossCounter = 0
        gambleCounter = 0

        # Running the loop indefinitely till either the stake amount becomes 0 or reaches the goal amount
        for i in range(bet_count):
            Gamble = random.randint(0, 1)
            # print(Gamble)
            gambleCounter += 1
            if Gamble == 1:
                stake += 1
                winCounter += 1
            else:
                stake -= 1
                lossCounter += 1

            if stake == goal:
                print(f"You have achieved your goal amount in {gambleCounter} bets/gambles")
                break
            elif stake == 0:
                print("You do not have any money left to continue!!!")

        # calculating percentage of wins and losses and printing the output
        win_percentage = (winCounter / gambleCounter) * 100
        loss_percentage = (lossCounter / gambleCounter) * 100
        print(f"You have won {winCounter} times out of {gambleCounter} and your winning percentage is {win_percentage}")
        print(f"You have lost {lossCounter} times out of {gambleCounter} and your losing percentage is {loss_percentage}")
        print(f"Final Amount : {stake}")
    else:
        print("The Goal has to be bigger than stake")

except ValueError:
    print("Please provide numeric input")

