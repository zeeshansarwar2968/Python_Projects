# Leap Year
# a. I/P -> Year, ensure it is a 4 digit number.
# b. Logic -> Determine if it is a Leap Year.
# c. O/P -> Print the year is a Leap Year or not.

# taking in user input to validate leap year
user_input = input("Please input the year to check for leap : ")

# initial conditional statement to check for size of user input and execute accordingly
if len(user_input) == 4:
    try:
        year = int(user_input)      # explicit type casting of input value to integer

        # if either ( year is divisible by 4 but not by 100 ) or ( if year is divisible by 400 )
        # condition is true, it is a leap year
        if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # Conditional block with logic to check for leap
            print(f"{year} is a leap year!!")
        else:
            print(f"{year} is not a leap year!!")
    except ValueError:
        print("Please provide numeric input.")
else:
    print("Please provide input in proper format.")
