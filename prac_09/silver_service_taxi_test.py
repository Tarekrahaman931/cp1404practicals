"""
CP1404/CP5632 Practical
Test SilverServiceTaxi class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""
    # Create a SilverServiceTaxi with fanciness of 2
    hummer = SilverServiceTaxi("Hummer", 200, 2)

    # Drive the taxi 18 km
    hummer.drive(18)

    # Print the taxi's details and the calculated fare
    print(hummer)
    print(f"Fare for 18 km: ${hummer.get_fare():.2f}")

    # Add another assert test for correctness
    assert hummer.get_fare() == 48.80, "Fare calculation is incorrect!"


if __name__ == "__main__":
    main()
