#!/usr/bin/python3
# 0-add_integer.py
""" Difines an integer addition function."""


def add_integer(a, b=98):
    """
    return addition of a and b.

    float arguments must be typecasted into integer before addition.

    Raises:
        TypeError: if either of a or b is a non-integer and non-float. 
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a) if type(a) == float else a
    b = int(b) if type(b) == float else b

    return a + b
