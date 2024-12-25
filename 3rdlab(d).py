#  Write a python script to print the multiplication table of a given number up
# to the specified limit using a for loop
num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))
for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")
