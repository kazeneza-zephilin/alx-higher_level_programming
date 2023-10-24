#!/usr/bin/python3


class Square:
    """
    square that define size attribute and area method with some
    restricted input
    """
    def __init__(self, size=0):
        """
        initialization of square functions
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
        """
        return self.__size ** 2
