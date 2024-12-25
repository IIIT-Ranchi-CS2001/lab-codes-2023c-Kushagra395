# Write a program to find the roots of a quadratic equation when the
# coefficients a, b and c are given ( assume that a, b and c are
# integers)
import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

d = b**2 - 4*a*c  # Discriminant

if d == 0:
    r1 = r2 = -b / (2*a)
    print(f"Roots are real and equal: R1 = R2 = {r1}")
elif d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Roots are real and distinct: R1 = {r1}, R2 = {r2}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-d) / (2*a)
    print(f"Roots are complex: R1 = {real_part} + {imaginary_part}i, R2 = {real_part} - {imaginary_part}i")
