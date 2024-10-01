def main():
    password = get_password()

def get_password():
    MIN_LENGTH = 8
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password must be at least {MIN_LENGTH} characters long.")
        password = input("Enter your password: ")
    return password


def print_asterisks(password):
    print('*' * len(password))


if __name__ == "__main__":
    main()
