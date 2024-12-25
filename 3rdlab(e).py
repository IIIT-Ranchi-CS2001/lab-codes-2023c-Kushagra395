# Write a python script to check whether all the characters present in a string
# are alphanumeric (uppercase letters, lowercase letters or digits) using for.
# Print True if all characters are alphanumeric. Otherwise print False.
string = input("Enter a string: ")
is_alphanumeric = all(char.isalnum() for char in string)
print(is_alphanumeric)
