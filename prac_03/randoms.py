import random

# Line 1: Produces a random integer between 5 and 20 (inclusive).
print(random.randint(5, 20))  # Example output: 13

# Smallest number possible: 5
# Largest number possible: 20

# Line 2: Produces a random number in the range (3, 10) with a step of 2 (i.e., 3, 5, 7, 9).
print(random.randrange(3, 10, 2))  # Example output: 7

# Smallest number possible: 3
# Largest number possible: 9
# Could line 2 have produced a 4? No, because the step is 2, so it can only produce 3, 5, 7, or 9.

# Line 3: Produces a random floating-point number between 2.5 and 5.5.
print(random.uniform(2.5, 5.5))  

# Smallest number possible: 2.5
# Largest number possible: 5.5

# Generate a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)  # Example output: 56
