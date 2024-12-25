# Redo question 2 without using zip and sorted functions.
students = []
names = input("Enter names: ").split()
roll_numbers = list(map(int, input("Enter roll numbers: ").split()))
marks = list(map(int, input("Enter marks: ").split()))

for i in range(len(names)):
    students.append((names[i], roll_numbers[i], marks[i]))

for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[i][2] < students[j][2]:
            students[i], students[j] = students[j], students[i]

print("Sorted students by marks (highest to lowest):")
for student in students:
    print(student)
