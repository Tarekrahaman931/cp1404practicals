"""
CP1404/CP5632 Practical
Test UnreliableCar class
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class."""
    # Create an UnreliableCar with 50% reliability
    unreliable_car = UnreliableCar("Unreliable", 100, 50)

    # Attempt to drive the car 10 times for 10 km each time
    print(f"Testing UnreliableCar '{unreliable_car.name}' with 50% reliability.")
    for i in range(1, 11):  # Loop for multiple test drives
        distance_driven = unreliable_car.drive(10)
        print(f"Attempt {i}: Tried to drive 10km, drove {distance_driven}km")
        print(unreliable_car)  # Display current state of the car

    # Create an UnreliableCar with 90% reliability
    reliable_car = UnreliableCar("Mostly Reliable", 100, 90)
    print(f"\nTesting UnreliableCar '{reliable_car.name}' with 90% reliability.")
    for i in range(1, 11):
        distance_driven = reliable_car.drive(10)
        print(f"Attempt {i}: Tried to drive 10km, drove {distance_driven}km")
        print(reliable_car)


if __name__ == "__main__":
    main()
