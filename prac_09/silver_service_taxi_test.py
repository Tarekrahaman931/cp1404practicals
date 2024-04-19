from silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi object
    my_silver_taxi = SilverServiceTaxi("Hummer", 200, 4)  # 4 times fancier

    # Drive the taxi for 18 km
    my_silver_taxi.drive(18)

    # Calculate and print the fare
    fare = my_silver_taxi.get_fare()
    print(f"Total fare: ${fare:.2f}")

    # Test if the fare calculation is correct
    assert fare == 48.78, "Fare calculation is incorrect"

if __name__ == "__main__":
    main()