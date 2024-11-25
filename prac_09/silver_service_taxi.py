"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from prac_09.taxi import Taxi  # Ensure the Taxi class is imported correctly


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with fanciness and flagfall."""

    flagfall = 4.50  # Class variable for the fixed flagfall charge

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        base_price_per_km = 1.23  # Default price_per_km as per Taxi requirements
        super().__init__(name, fuel, base_price_per_km)  # Pass the base price to Taxi's constructor
        self.price_per_km *= fanciness  # Scale price_per_km by fanciness
        self.fanciness = fanciness  # Store fanciness as an instance variable

    def get_fare(self):
        """Calculate the fare including flagfall."""
        return round(super().get_fare() + self.flagfall, 1)  # Add flagfall and round to the nearest 10c

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
