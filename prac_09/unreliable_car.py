"""
CP1404/CP5632 Practical
UnreliableCar class
"""
import random
from prac_09.car import Car  # Ensure the Car class is imported correctly

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive the car a given distance if it's reliable enough.
        Generate a random number and compare it to reliability.
        """
        if random.uniform(0, 100) < self.reliability:  # Random chance to drive
            return super().drive(distance)  # Use the parent class drive method
        return 0  # If not reliable, the car doesn't drive
