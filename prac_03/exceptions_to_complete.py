"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # TODO: Set is_finished to True to exit the loop when a valid integer is entered
    except ValueError:  # TODO: Add the exception you want to catch after except
        print("Please enter a valid integer.")

print("Valid result is:", result)
