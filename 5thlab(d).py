# Create a program that manages employee salaries in a company using a
# dictionary. The dictionary should contain at least 5 employees, with their
# names as keys and their respective salaries as values [take user input data].
# Implement a sorting algorithm to arrange the employees in descending order
# based on their salaries without using any built-in sorting functions, and
# display the sorted list along with their salaries and rank\
employees = {}
for _ in range(5):
    name = input("Enter employee name: ")
    salary = int(input(f"Enter salary for {name}: "))
    employees[name] = salary

sorted_employees = sorted(employees.items(), key=lambda x: x[1], reverse=True)

print("Employees sorted by salary:")
for rank, (name, salary) in enumerate(sorted_employees, 1):
    print(f"{rank}. {name}: Rs. {salary}")
