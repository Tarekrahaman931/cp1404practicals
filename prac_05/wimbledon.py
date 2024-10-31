"""
CP1404/CP5632 Practical
Wimbledon Champions Data Processing
Estimate: 40 minutes
"""

import csv


def read_csv_file(filename):
    """
    Reads the CSV file and returns the data as a list of lists.
    """
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        data = [row for row in reader]
    return data


def process_champions(data):
    """
    Processes the champions data and returns a dictionary with champion names and their respective win counts.
    """
    champions = {}
    for row in data:
        name = row[0]
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions


def display_champions(champions):
    """
    Displays the champions and their win counts.
    """
    print("Wimbledon Champions:")
    for name, wins in champions.items():
        print(f"{name} {wins}")


def extract_countries(data):
    """
    Extracts the countries of champions and returns a set of unique country codes.
    """
    countries = set()
    for row in data:
        countries.add(row[1])
    return countries


def display_countries(countries):
    """
    Displays the countries of champions in alphabetical order.
    """
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def main():
    filename = "wimbledon.csv"
    data = read_csv_file(filename)

    champions = process_champions(data)
    display_champions(champions)

    countries = extract_countries(data)
    display_countries(countries)


if __name__ == "__main__":
    main()
