# Write a python script using map, lambda and filter functions to do the following
# operations on a user inputted comma separated strings: E.g.: “Tom 25 Rahu22
# 2@$”
# ● To find all the letters given in the string and to convert them to uppercase
# ○ o/p: [‘TOM’]
# ● To find all the digits
string = input("Enter a string: ")

# Uppercase letters
uppercase = list(map(str.upper, filter(str.isalpha, string.split())))
print("Uppercase letters:", uppercase)

# Squares of digits
squares = list(map(lambda x: int(x)**2, filter(str.isdigit, string.split())))
print("Squares of digits:", squares)

# Alphanumeric characters
alphanumeric = list(filter(str.isalnum, string.split()))
print("Alphanumeric characters:", alphanumeric)
