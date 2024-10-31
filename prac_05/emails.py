"""
CP1404/CP5632 Practical
Emails and Name Storage Program
Estimate: 30 minutes
"""


def extract_name_from_email(email):
    """Extract the user's name from the email."""
    prefix = email.split('@')[0]  # Get the part before '@'
    parts = prefix.split('.')  # Split on periods
    name = " ".join(parts).title()  # Join the parts and title-case them
    return name


def main():
    """Main program to collect and display emails and names."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        # Ask the user to confirm the extracted name
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation != "" and confirmation != 'y':
            # If user says no, ask for their correct name
            name = input("Name: ")

        email_to_name[email] = name

        # Ask for the next email
        email = input("Email: ")

    # Print the emails and names
    print("\nStored information:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
