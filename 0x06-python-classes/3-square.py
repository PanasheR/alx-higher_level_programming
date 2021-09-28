#!/usr/bin/python3


class Square:
    """empty class that defines a square"""

    def __init__(self, size=0):
        """Args:
            size (int): length of side of square
        """

        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')

        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns area of square
            Yields:
                int: area
        """
        return self.__size * self.__size
