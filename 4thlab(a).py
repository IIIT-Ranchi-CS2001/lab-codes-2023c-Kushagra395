#  Find the number of palindrome words in the given sentence without defining
# any new function (feel free to use python’s in-built functions).
sentence = input("Enter a sentence: ").split()
palindromes = [word for word in sentence if word == word[::-1]]
print(f"Number of palindrome words: {len(palindromes)}")
