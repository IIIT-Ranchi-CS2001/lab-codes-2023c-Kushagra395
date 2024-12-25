# Enter the coordinates of two points on the cartesian plane (take user input
# using comprehension). Find the equation of the straight line passing through
# these points
p1 = tuple(map(float, input("Enter point 1 (x y): ").split()))
p2 = tuple(map(float, input("Enter point 2 (x y): ").split()))

if p2[0] != p1[0]:
    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    print(f"Equation: y - {p1[1]} = {slope}(x - {p1[0]})")
else:
    print("The line is vertical: x =", p1[0])
