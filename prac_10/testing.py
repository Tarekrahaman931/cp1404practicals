"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_phrase_as_sentence('hello')
    'Hello.'
    >>> format_phrase_as_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase_as_sentence('this is a test')
    'This is a test.'
    """
    phrase = phrase.strip()  # Remove leading/trailing spaces
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase.capitalize()


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # this test now passes because repeat_string has been fixed
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # assert statements to check if Car sets the fuel correctly
    car_with_default_fuel = Car()
    assert car_with_default_fuel.fuel == 0, "Car does not set default fuel correctly"

    car_with_custom_fuel = Car(fuel=10)
    assert car_with_custom_fuel.fuel == 10, "Car does not set custom fuel correctly"


run_tests()

# Uncomment the following line to run the doctests
doctest.testmod()
