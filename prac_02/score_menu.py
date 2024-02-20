"""A program that provides a option for various operations on scores."""

def get_valid_score():
    """Function to get a valid score (0-100 inclusive)."""
    score = -1  # Initialize score to an invalid value
    while not (0 <= score <= 100):
        try:
            score = int(input("Enter a score (0-100): "))
            if not (0 <= score <= 100):
                print("Score must be between 0 and 100, inclusive.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return score

def print_result(score):
    """Function to print the result based on the score."""

    pass

def show_stars(score):
    """Function to print stars based on the score."""
    print("*" * score)

def do_stuff():
    """Function to perform various operations on scores."""
    score = get_valid_score()
    choice = ''

    while choice != 'Q':
        print("\nMENU:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Goodbye!")
        else:
            print("Invalid choice. Please enter G, P, S, or Q.")

def main():
    """Main function to run the program."""
    do_stuff()

if __name__ == "__main__":
    main()
