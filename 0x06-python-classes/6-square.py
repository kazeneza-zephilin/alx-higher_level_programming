#!/usr/bin/python3
"""Module square"""


class Square:
    """
    Represents a square with attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    Some attributes are protected from input.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes instances of the Square class.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If the size is not an integer or if the position
                is not a tuple.
            ValueError: If the size is less than 0.
        """
        if self.__validate_size(size):
            self.__size = size
        if self.__validate_pos(position):
            self.__position = position

    @property
    def size(self):
        """
        Gets the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the new size value is not an integer.
            ValueError: If the new size value is less than 0.
        """
        if self.__validate_size(value):
            self.__size = value

    @property
    def position(self):
        """
        Gets the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position attribute.

        Args:
            value (tuple): The new position value.

        Raises:
            TypeError: If the new position value is not a tuple of 2
                positive integers.
        """
        if self.__validate_pos(value):
            self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters, considering position (x, y)
        offsets.
        """
        i = 0
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        i = 0
        for i in range(0, self.__size):
            j = 0
            x_pad = 0
            for x_pad in range(0, self.__position[0]):
                print(" ", end='')
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

    def __validate_pos(self, position):
        """
        Validates the position, checking for type errors.

        Args:
            position (tuple): The position to be validated.

        Returns:
            bool: True if the position is valid, False otherwise.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        if not isinstance(position, type((0, 0))):
            raise TypeError("position must be a tuple of 2 positive integers")
            return False
        return True
