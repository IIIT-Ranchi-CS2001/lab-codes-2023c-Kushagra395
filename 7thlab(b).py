# Write a python script to
# 1. Form a list of K random numbers within a limit N where K and N are
# set by the user. Minimum value of K should be 10.
# 2. Define a function (or two functions) to return the composite numbers
# and prime numbers of this list as two separate lists.
# 3. Determine the square of all prime numbers and square root of all
# composite numbers
# 4. Plot both prime numbers Vs their squares and composites Vs their
# square roots on the same figure object as scatterplots. ( two different
# subplots on the same figure object)

import random
import math

# Random number generation
k = int(input("Enter K (minimum 10): "))
n = int(input("Enter N: "))
numbers = random.sample(range(1, n+1), k)

# Prime and composite classification
primes = [x for x in numbers if all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1)) and x > 1]
composites = [x for x in numbers if x not in primes]

# Squares and square roots
prime_squares = [x**2 for x in primes]
composite_sqrts = [math.sqrt(x) for x in composites]

# Plotting
plt.figure()
plt.subplot(1, 2, 1)
plt.scatter(primes, prime_squares)
plt.title("Prime Numbers vs Squares")
plt.subplot(1, 2, 2)
plt.scatter(composites, composite_sqrts)
plt.title("Composite Numbers vs Square Roots")
plt.show()
