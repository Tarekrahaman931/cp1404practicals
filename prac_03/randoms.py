import random

# What did you see on line 1?
# Answer: A random integer between 5 and 20, inclusive.

# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 5 and the largest is 20.

print(random.randint(5, 20))  # line 1

# What did you see on line 2?
# Answer: A random integer from the range [3, 10) with a step of 2.

# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 3 and the largest is 9.

# Could line 2 have produced a 4?
# Answer: No, because the step size is 2, so it will skip 4.

print(random.randrange(3, 10, 2))  # line 2

# What did you see on line 3?
# Answer: A random float between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 2.5 and the largest is 5.5.

print(random.uniform(2.5, 5.5))  # line 3

# Write code to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
