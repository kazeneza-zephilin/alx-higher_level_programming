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

    @property
    def size(self):
        """
        Retriving the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size value setter
        """
        if self.__validate_size(value):
            self.__size = value

    def area(self):

        """
        compute the area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        print square with character #
        """
        i = 0
        j = 0
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        """
        checking the errors
        """
        if type(size) != int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            return True
        return False
