"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status, with function
"""

def main():
    """Get a numeric score and display its status."""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()