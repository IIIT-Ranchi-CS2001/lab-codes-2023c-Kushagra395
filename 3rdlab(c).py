# Write a python script to print the first n terms of the Fibonacci series using
# while loop
n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
print("Fibonacci series:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
