# Generate two tuples to represent two distinct points in space. (Three
# dimensional geometry). Determine the Euclidean distance between the two.
import math

p1 = tuple(map(float, input("Enter coordinates of point 1 (x y z): ").split()))
p2 = tuple(map(float, input("Enter coordinates of point 2 (x y z): ").split()))

distance = math.sqrt(sum((c1 - c2)**2 for c1, c2 in zip(p1, p2)))
print(f"Euclidean distance: {distance}")
