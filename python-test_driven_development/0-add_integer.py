#!/usr/bin/python3
"""
In this package you will be able to see how 2 numbers add up. Valid number
types are float or integer. Any other data type will show an exception.
Floats are converted to integers by taking the first digit, so you can do
the addition only with integers.
"""


def add_integer(a, b=98):
    """
    The function add_integer is a function which allows 2 parameters, “a”
    will be a number to be added with “b”.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
