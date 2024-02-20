# Write the user's name to a file
name = input("Enter your name: ")
with open("name.txt", 'w') as file:
    file.write(name)


with open("name.txt", 'r') as file:
    name = file.read()
print(f"Your name is {name}")

with open("numbers.txt", 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
    total = number1 + number2
print("The sum of the first two numbers is:", total)

total = 0
with open("numbers.txt", 'r') as file:
    for line in file:
        total += int(line)
print("The total for all numbers is:", total)
