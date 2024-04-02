# myguitars.py
from guitar import Guitar

def load_guitars(file_name):
    guitars = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"{file_name} not found. No guitars loaded.")
    return guitars

def save_guitars(guitars, file_name):
    with open(file_name, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def main():
    file_name = "guitars.csv"
    guitars = load_guitars(file_name)

    print("All guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()
    print("\nGuitars sorted by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)

    # Add new guitars
    while True:
        name = input("Enter guitar name (or enter to quit): ")
        if not name:
            break
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))

    save_guitars(guitars, file_name)
    print("Guitars saved to file.")

if __name__ == "__main__":
    main()
