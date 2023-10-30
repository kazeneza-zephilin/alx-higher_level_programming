#!/usr/bin/python3
"""square module"""


class Square:
    """
    class square that has attributes:
        size
    some attributes are protected from input.
    """

    def __init__(self, size=0):
        """
        initialization function for our square class

        Args:
            size (int) size of square.

        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is less than 0.
        """
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        """
        getter for size attribute

        Returns:
            int: the size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method for updating the size attribute.

        Args:
            value (int): the new size value.

        Raises:
            TypeError: If the new size value is not an integer.
            ValueError: If the new size value is less than 0.
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        calculates the area of the square

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __validate_size(self, size):
        """
        validates the size, checking for errors

        Args:
            size (int): The size to be validated.

        Returns:
            bool: True if the size is valid, False otherwise.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
