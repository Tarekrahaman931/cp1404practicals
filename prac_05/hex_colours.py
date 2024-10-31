"""
CP1404/CP5632 Practical
Hexadecimal colour lookup program
"""

# Dictionary containing some hexadecimal colour codes
HEX_COLOURS = {
    "Absolute Zero": "#0048ba",
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Alizarin Crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine1": "#7fffd4"
}

# Get user input and handle it
colour_name = input("Enter colour name: ").title()  # Convert input to title case
while colour_name != "":
    try:
        print(f"{colour_name} is {HEX_COLOURS[colour_name]}")
    except KeyError:
        print("Invalid colour name")

    # Ask for input again
    colour_name = input("Enter colour name: ").title()

print("Goodbye!")
