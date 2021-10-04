#!/usr/bin/python3


class Rectangle:
    """empty class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns width as private """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value as private from user"""
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Returns height as private """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height value as private from user"""
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Function that returns area"""
        return self.__height * self.__width

    def perimeter(self):
        """Function that returns perimeter"""
        if (self.__height == 0 or self.__width == 0):
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Function that prints rectangle of '#' characaters"""
        my_string = ""

        if (self.__height == 0 or self.__width == 0):
            return my_string

        for i in range(self.__height):
            for j in range(self.__width):
                my_string += '#'
            if (i == self.__height - 1 and j == self.__width - 1):
                break
            my_string += '\n'

        return my_string

    def __repr__(self):
        """Prints class and arguments passed to methods inside it"""
        name_string = 'Rectangle(' + str(self.__width) + ', ' \
                      + str(self.__height) + ')'
        return name_string
