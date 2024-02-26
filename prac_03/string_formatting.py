"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

print("My guitar: " + name + ", first made in " + str(year))

print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

print(f"My {name} was first made in {year} (that's right, {year}!)")

print("My {} would cost ${:,.2f}".format(name, cost))
print(f"My {name} would cost ${cost:,.2f}")

numbers = [1, 19, 123, 456, -25]

for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

print(f"{year} {name} for about ${cost:,.0f}!")
for i in range(0, 151, 50):
    print(f"{i:3}")
