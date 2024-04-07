"""
Hexadecimal Colour Code Lookup
"""

COLOUR_CODES = {
    "Acid Green": "#b0bf1a",
    "AliceBlue": "#f0f8ff",
    "Alizarin crimson": "#e32636",
    "Amaranth": "#e52b50",
    "Amber": "#ffbf00",
    "Amethyst": "#9966cc",
    "AntiqueWhite": "#faebd7",
    "AntiqueWhite1": "#ffefdb",
    "AntiqueWhite2": "#eedfcc",
    "AntiqueWhite3": "#cdc0b0",
    "AntiqueWhite4": "#8b8378",
    "Apricot": "#fbceb1"
}

def lookup_colour(name):
    try:
        return COLOUR_CODES[name]
    except KeyError:
        return "Invalid colour name"

# Main program loop
while True:
    color_name = input("Enter a colour name (or blank to stop): ").capitalize()
    if color_name == "":
        break
    else:
        print(lookup_colour(color_name))

