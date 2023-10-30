#!/usr/bin/python3
"""class module"""


class Square:
    """Square with size of integer type with restricted
    negative integer
    """
    def __init__(self, size=0):
        """
        initialization of class attributes
        args:
        size:side length
        """
        if type(size) == int:
            self.__size = size

        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
