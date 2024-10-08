try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero!")  # Handle the zero case before division
    else:
        fraction = numerator / denominator
        print(f"The result is: {fraction}")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
