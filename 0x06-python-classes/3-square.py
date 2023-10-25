#!/usr/bin/python3
"""
class module
"""


class Square:
    """
    square that define size attribute and area method with some
    restricted input
    """
    def __init__(self, size=0):
        """
        initialization of square functions
        args:
            size (int): length of square
        Raises:
            TypeError:  If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        """
        compute the area of square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2
