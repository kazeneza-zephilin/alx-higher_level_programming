#!/usr/bin/python3
"""class square module"""


class Square:
    """
    Represents a square with attributes:
        size (int): The size of the square.
    Attributes are protected from direct access.
    """

    def __init__(self, size=0):
        """
        Initializes instances of the Square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for updating the size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the new size value is not an integer.
            ValueError: If the new size value is less than 0.
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square using '#' characters.
        """
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        """
        Validates the size, checking for errors.

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
