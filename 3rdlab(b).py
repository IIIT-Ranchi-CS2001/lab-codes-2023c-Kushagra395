#  Write a python script to find the sum of the digits of the given number using
# a while loop. Display the number and the sum.
num = int(input("Enter a number: "))
total = 0
while num > 0:
    total += num % 10
    num //= 10
print(f"Sum of digits: {total}")
