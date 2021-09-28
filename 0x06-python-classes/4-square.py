#!/usr/bin/python3


class Square:
    """empty class that defines a square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Returns size as private """
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError('size must be an integer')

        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Returns area of square
            Yields:
                int: area
        """
        return self.__size * self.__size
