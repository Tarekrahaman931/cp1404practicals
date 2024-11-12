import csv
from guitar import Guitar


def main():
    """Main function to read and display guitars, then add new ones."""
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars)

    # Sort by year and display sorted guitars
    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    # Add new guitars from user input
    add_new_guitars(guitars)

    # Save all guitars back to file
    save_guitars("guitars.csv", guitars)


def load_guitars(filename):
    """Read guitar data from a file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row[0], int(row[1]), float(row[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display all guitars."""
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    """Prompt user to add new guitars until they choose to stop."""
    print("\nAdd new guitars (leave name blank to finish):")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"Added {new_guitar}")


def save_guitars(filename, guitars):
    """Save all guitars to a file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
    print("\nGuitars saved to file.")


if __name__ == "__main__":
    main()
