# User Input and Replace String Template “Hello <<UserName>>, How are you?”
# a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
# b. Logic -> Replace <<UserName>> with the proper name
# c. O/P -> Print the String with User Name

# Taking in the the input from user
user_name = input("Please input user-name : ")

# Starting a conditional block to check the length of the string
if len(list(user_name)) >= 3:
    # using f-string to interpolate the username and display the output
    print(f"Hello {user_name.capitalize()}, How are you?")
else:
    print("Please provide proper username with at least 3 characters")

