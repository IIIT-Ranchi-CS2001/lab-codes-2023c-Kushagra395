# Generate three lists using list comprehension. List of names, list of Roll nos
# and list of marks for Physics exam for all students of the class. Create a list
# of tuples using the zip function where each tuple carries individual student
# details. Sort the list of tuples using a sorted function by keeping Marks as the
# key for sorti
names = input("Enter names: ").split()
roll_numbers = list(map(int, input("Enter roll numbers: ").split()))
marks = list(map(int, input("Enter marks: ").split()))

students = list(zip(names, roll_numbers, marks))
sorted_students = sorted(students, key=lambda x: x[2], reverse=True)

print("Sorted students by marks (highest to lowest):")
for student in sorted_students:
    print(student)
