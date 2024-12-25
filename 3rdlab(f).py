# Write a python script to find the number of occurrences of a particular
# character present in the given string using a loop. (Don’t use string
# methods).
string = input("Enter a string: ")
char = input("Enter the character to count: ")
count = 0
for c in string:
    if c == char:
        count += 1
print(f"Occurrences of '{char}': {count}")
