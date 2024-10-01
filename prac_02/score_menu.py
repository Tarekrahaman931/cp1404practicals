def main():
    """Main function to run the score menu."""
    score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Choose an option: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_score_status(score)
            print(f"Your score is {score}. Result: {result}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Goodbye! Thanks for using the program.")
            break
        else:
            print("Invalid option. Please choose a valid option from the menu.")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = int(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = int(input("Enter a valid score (0-100): "))
    return score


def determine_score_status(score):
    """Determine the status of a score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    """Print as many stars as the score."""
    print("*" * score)


if __name__ == "__main__":
    main()
