# Generate 2 lists (course code and course name). create a new list with both
# course code and name like["CS1001:Python"
# ,...]
codes = input("Enter course codes: ").split()
names = input("Enter course names: ").split()
courses = [f"{code}:{name}" for code, name in zip(codes, names)]
print(courses)
