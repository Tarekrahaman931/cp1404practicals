class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self, current_year):
        return current_year - self.year

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50

def test_guitar_methods():
    # Create a Guitar object
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)

    current_year = 2022
    gibson_age = gibson.get_age(current_year)
    expected_gibson_age = 100
    print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {gibson_age}")

    another_guitar = Guitar("Another Guitar", 2013, 500)

    another_guitar_age = another_guitar.get_age(current_year)
    expected_another_guitar_age = 9
    print(f"{another_guitar.name} get_age() - Expected {expected_another_guitar_age}. Got {another_guitar_age}")

    gibson_vintage = gibson.is_vintage(current_year)
    expected_gibson_vintage = True
    print(f"{gibson.name} is_vintage() - Expected {expected_gibson_vintage}. Got {gibson_vintage}")

    another_guitar_vintage = another_guitar.is_vintage(current_year)
    expected_another_guitar_vintage = False
    print(f"{another_guitar.name} is_vintage() - Expected {expected_another_guitar_vintage}. Got {another_guitar_vintage}")

if __name__ == "__main__":
    test_guitar_methods()
