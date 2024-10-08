is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Mark as finished once a valid integer is entered
    except ValueError:  # Catch only ValueError
        print("Please enter a valid integer.")
print("Valid result is:", result)
