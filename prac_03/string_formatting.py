"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# The 'old' manual way to format text with string concatenation (avoid this method):
print("My guitar: " + name + ", first made in " + str(year))

# A better approach using str.format() (only use this if necessary):
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Preferred method with f-string formatting (introduced in Python 3.6):
print(f"My {name} was first made in {year} (that's right, {year}!)")

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))  # str.format version
print(f"My {name} would cost ${cost:,.2f}")  # preferred f-string version

# Aligning columns using width after the colon:
numbers = [1, 19, 123, 456, -25]
for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# Producing the required output with f-string formatting:
# "1922 Gibson L-5 CES for about $16,036!"
print(f"{year} {name} for about ${cost:,.0f}!")

# Using a for loop with range and f-string formatting for right-aligned output:
for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:4}")
