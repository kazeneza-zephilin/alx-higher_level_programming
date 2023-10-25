#!/usr/bin/python3
"""python bytecodes decripty"""

import math

class MagicClass:
    """A class representing a MagicClass with radius attribute and methods
    to calculate area and circumference.
    """

    def __init__(self, radius):
        """Initialize the MagicClass with a radius.

        Args:
            radius (int or float): The radius of the circle.

        Raises:
            TypeError: If radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self._MagicClass__radius
