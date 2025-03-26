#!/usr/bin/python3
"""
    Adds two integers.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
"""


def add_integer(a, b=98):
    """This function adds two integers"""
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
