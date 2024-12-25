# Enter the following details of a student at run time: - Name, Roll
# number and marks secured for Mathematics Examination out of 100.
# Write a python script to display student details as show
name = input("Enter name: ")
roll_number = input("Enter roll number: ")
marks = int(input("Enter marks (out of 100): "))

if marks >= 90:
    grade, remark = 10, "OUTSTANDING"
elif marks >= 80:
    grade, remark = 9, "VERY GOOD"
elif marks >= 70:
    grade, remark = 8, "GOOD"
elif marks >= 60:
    grade, remark = 7, "AVERAGE"
elif marks >= 50:
    grade, remark = 6, "PASS"
else:
    grade, remark = 0, "FAIL"

print(f"""
Name: {name}
Roll Number: {roll_number}
Marks: {marks}
Grade Point: {grade}
Remark: {remark}
""")
