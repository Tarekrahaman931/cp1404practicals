"""
CP1404 - Inheritance Practical
Testing the Taxi class.
"""

from prac_09.taxi import Taxi 

def main():
    """Test the Taxi class."""
    # Create an instance of Taxi
    my_taxi = Taxi("Prius 1", 100, 1.23)  # Include price_per_km as required by the current Taxi class

    # Drive the taxi for 40 km
    distance_driven = my_taxi.drive(40)

    # Print the details of the taxi and the fare
    print(f"After driving {distance_driven}km:")
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Start a new fare and drive for 100 km
    my_taxi.start_fare()
    distance_driven = my_taxi.drive(100)

    # Print the updated details of the taxi and the fare
    print(f"\nAfter starting a new fare and driving {distance_driven}km:")
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()
