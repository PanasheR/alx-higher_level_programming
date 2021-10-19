#!/usr/bin/python3

"""Importing Base class"""
from models.base import Base


class Rectangle(Base):
    """Class that defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns width as private """
        return self.__width

    @width.setter
    def width(self, width):
        """Sets width value as private from user"""
        if type(width) is not int:
            raise TypeError('width must be an integer')

        if width <= 0:
            raise ValueError('width must be > 0')

        self.__width = width

    @property
    def height(self):
        """Returns height as private """
        return self.__height

    @height.setter
    def height(self, height):
        """Sets height value as private from user"""
        if type(height) is not int:
            raise TypeError('height must be an integer')

        if height <= 0:
            raise ValueError('height must be > 0')

        self.__height = height

    @property
    def x(self):
        """Returns x as private """
        return self.__x

    @x.setter
    def x(self, x):
        """Sets x value as private from user"""
        if type(x) is not int:
            raise TypeError('x must be an integer')

        if x < 0:
            raise ValueError('x must be >= 0')

        self.__x = x

    @property
    def y(self):
        """Returns y as private """
        return self.__y

    @y.setter
    def y(self, y):
        """Sets y value as private from user"""
        if type(y) is not int:
            raise TypeError('y must be an integer')

        if y < 0:
            raise ValueError('y must be >= 0')

        self.__y = y

    def area(self):
        """public method that returns the area of Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """
        public method that prints the Rectangle instance with the character #
        """
        if self.__y > 0:
            for k in range(self.__y):
                print()

        for i in range(self.__height):
            if self.__x > 0:
                for s in range(self.__x):
                    print(' ', end='')

            for j in range(self.__width):

                if i == self.__height - 1 and j == self.__width - 1:
                    print('#')
                    break
                if j == self.__width - 1:
                    print('#')
                    continue

                print('#', end='')

    def __str__(self):
        """
        overriding the __str__ method so that it returns [Rectangle] (<id>)
        <x>/<y> - <width>/<height>
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        public method that assigns an updated  argument to each attribute
        for an instance
        """
        passed_args = [k for k in args]
        passed_kwargs = {k: kwargs[k] for k in kwargs}

        if len(passed_args) > 0:

            arguments = ["id", "width", "height", "x", "y"]

            arg_dict = {k: v for (k, v) in zip(arguments, passed_args)}

            if 'width' in arg_dict:
                self.width = arg_dict['width']

            if 'height' in arg_dict:
                self.height = arg_dict['height']

            if 'x' in arg_dict:
                self.x = arg_dict['x']

            if 'y' in arg_dict:
                self.y = arg_dict['y']

            if 'id' in arg_dict:
                super().__init__(arg_dict['id'])

        if len(passed_args) == 0 and len(passed_kwargs) > 0:
            if 'width' in passed_kwargs:
                self.width = passed_kwargs['width']

            if 'height' in passed_kwargs:
                self.height = passed_kwargs['height']

            if 'x' in passed_kwargs:
                self.x = passed_kwargs['x']

            if 'y' in passed_kwargs:
                self.y = passed_kwargs['y']

            if 'id' in passed_kwargs:
                super().__init__(passed_kwargs['id'])

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation of class
        Rectangle
        """
        curr_args = {"id": self.id, "width": self.width,
                     "height": self.height, "x": self.x, "y": self.y}

        return curr_args
