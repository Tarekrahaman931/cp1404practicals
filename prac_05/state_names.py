"""
CP1404/CP5632 Practical
State names in a dictionary
This file is reformatted according to PEP 8 conventions
"""

# Dictionary containing Australian state abbreviations and names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Print all states and names, neatly lined up
for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code:3} is {state_name}")

# Get user input and check the state code using EAFP approach
state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        # Attempt to retrieve the state name using the provided code
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")

    # Ask for input again and allow lowercase entries
    state_code = input("Enter short state: ").upper()

