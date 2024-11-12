"""
CP1404/CP5632 Practical - guitar
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar using string formatting."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Calculate and return the age of the guitar in years."""
        current_year = 2024  # Use current year for age calculation
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50 or more years old)."""
        return self.get_age() >= 50