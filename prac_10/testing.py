"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06 .car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.

    >>> repeat_string("Python", 1)
    'Python'
    >>> repeat_string("hi", 2)
    'hi'
    >>> repeat_string("yo", 2)
    'yo yo'
    """
    return " ".join([s] * n)


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # Test if Car sets the fuel correctly
    test_car_default_fuel = Car()
    assert test_car_default_fuel.fuel == 0, "Car does not set default fuel correctly"

    test_car_custom_fuel = Car(fuel=10)
    assert test_car_custom_fuel.fuel == 10, "Car does not set custom fuel correctly"


run_tests()

# Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


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


def format_sentence(phrase):
    """Format a phrase as a sentence, starting with a capital and ending with a single full stop.

    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('this is a test phrase')
    'This is a test phrase.'
    """
    if not phrase:
        return ""
    formatted_phrase = phrase.capitalize()
    if formatted_phrase[-1] != ".":
        formatted_phrase += "."
    return formatted_phrase


doctest.testmod()
