# Leap Year
# a. I/P -> Year, ensure it is a 4 digit number.
# b. Logic -> Determine if it is a Leap Year.
# c. O/P -> Print the year is a Leap Year or not.

user_input = input("Please input the year to check for leap : ")

if len(user_input) == 4:
    try:
        year = int(user_input)
        if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # Conditional block
            print(f"{year} is a leap year!!")
        else:
            print(f"{year} is not a leap year!!")
    except ValueError:
        print("Please provide numeric input.")
else:
    print("Please provide input in proper format.")
