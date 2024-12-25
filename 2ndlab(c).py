# Write a python script to enter any string at run time and check
# whether it is a palindrome or not.
string = input("Enter a string: ")
print("Palindrome" if string == string[::-1] else "Not a palindrome")
