# Enter three lists using list comprehension: Customer name, Customer ID,
# and shopping points. Construct a list of tuples with and without using
# built-in function zip().
# Using zip()
names = input("Enter customer names: ").split()
ids = list(map(int, input("Enter customer IDs: ").split()))
points = list(map(int, input("Enter shopping points: ").split()))

# Using zip
tuples_with_zip = list(zip(names, ids, points))
print("Tuples using zip():", tuples_with_zip)

# Without using zip
tuples_without_zip = []
for i in range(len(names)):
    tuples_without_zip.append((names[i], ids[i], points[i]))
print("Tuples without zip():", tuples_without_zip)
