# W AP to count the number of each character present in a string using the
# concept of a dictionary.
string = input("Enter a string: ")
char_count = {}

for char in string:
    char_count[char] = char_count.get(char, 0) + 1

print("Character counts:", char_count)
