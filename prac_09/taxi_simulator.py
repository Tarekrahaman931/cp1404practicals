"""
CP1404/CP5632 Practical
Taxi Simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Run the taxi simulator program."""
    # Create taxis
    taxis = [
        Taxi("Prius", 100, 1.23),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]

    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    print(MENU)

    while True:
        choice = input(">>> ").lower()
        if choice == "q":
            break
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Display available taxis and allow the user to choose one."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid taxi choice")
        return None


def drive_taxi(taxi):
    """Drive the chosen taxi and calculate the trip cost."""
    try:
        distance = int(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0.0

    distance_driven = taxi.drive(distance)
    trip_cost = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
    taxi.start_fare()  # Reset the fare for the next trip
    return trip_cost


def display_taxis(taxis):
    """Display the list of available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == "__main__":
    main()
