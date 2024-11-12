"""
File and class example - reads a file, stores data in objects of custom class.
"""

import csv
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading using 'with' statement for better practice
    with open('languages.csv', 'r') as in_file:
        # Read the header line
        in_file.readline()
        # All other lines are language data
        for line in in_file:
            # Strip newline from end and split it into parts (CSV)
            parts = line.strip().split(',')
            # Convert Reflection and Pointer Arithmetic to Boolean
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[4] == "Yes"
            # Create a ProgrammingLanguage object
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
            # Add the language object to the list
            languages.append(language)

    # Display all languages using their __str__ method
    for language in languages:
        print(language)


if __name__ == "__main__":
    main()

