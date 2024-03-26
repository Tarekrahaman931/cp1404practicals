def extract_name(email):
    """
    Extracts a name from an email address.
    """
    # Split the email address at '@' symbol to get the username part
    username = email.split('@')[0]

    # Split the username at '.' symbols and capitalize each part
    parts = [part.capitalize() for part in username.split('.')]

    # Join the parts to form the name
    name = ' '.join(parts)

    return name


# Create an empty dictionary to store email and name pairs
user_data = {}

# Main loop to gather user data
while True:
    email = input("Email: ")
    if email == "":
        break
    else:
        name = extract_name(email)
        is_correct = input(f"Is your name {name}? (Y/n) ").lower()
        if is_correct == "" or is_correct == "y":
            user_data[email] = name
        else:
            name = input("Name: ").title()
            user_data[email] = name

# Print the collected user data
for email, name in user_data.items():
    print(f"{name} ({email})")
