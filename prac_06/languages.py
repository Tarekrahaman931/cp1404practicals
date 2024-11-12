"""
CP1404/CP5632 Practical
"""

from programming_language import ProgrammingLanguage

def main():
    """Create and display details of programming languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Print language details
    print(python)
    print(ruby)
    print(visual_basic)

    # Create a list of programming languages
    languages = [python, ruby, visual_basic]

    # Print the names of all dynamically typed languages
    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()
