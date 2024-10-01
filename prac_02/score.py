import random

def main():
    """Main function to ask user for score and determine result."""
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(f"Your score is {result}.")


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


if __name__ == "__main__":
    main()
