"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Questions:
# 1. When will a ValueError occur?
#    Answer: A ValueError will occur if the user enters a non-integer value for numerator or denominator.

# 2. When will a ZeroDivisionError occur?
#    Answer: A ZeroDivisionError will occur if the user enters 0 as the denominator.

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#    Answer: Yes, by adding a check before performing the division operation.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (not equal to zero): "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
