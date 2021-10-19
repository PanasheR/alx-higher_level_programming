#!/usr/bin/python3

"""Importing Rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns size as public"""
        return super().width

    @size.setter
    def size(self, size):
        """Sets and assigns size for width and height"""

        self.width = size
        self.height = size

    def __str__(self):
        """
        overriding the __str__ method so that it returns [Square] (<id>)
        <x>/<y> - <size>
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id,
                                             super().x,
                                             super().y,
                                             super().width)

    def update(self, *args, **kwargs):
        """
        public method that assigns an updated argument to each attribute
        for an instance
        """
        passed_args = [k for k in args]
        passed_kwargs = {k: kwargs[k] for k in kwargs}

        if len(passed_args) > 0:

            arguments = ["id", "size", "x", "y"]

            arg_dict = {k: v for (k, v) in zip(arguments, passed_args)}

            if 'size' in arg_dict:
                self.size = arg_dict['size']

            if 'x' in arg_dict:
                self.x = arg_dict['x']

            if 'y' in arg_dict:
                self.y = arg_dict['y']

            if 'id' in arg_dict:
                self.id = arg_dict['id']

            return

        if len(passed_args) == 0 and len(passed_kwargs) > 0:
            if 'size' in passed_kwargs:
                self.size = passed_kwargs['size']

            if 'x' in passed_kwargs:
                self.x = passed_kwargs['x']

            if 'y' in passed_kwargs:
                self.y = passed_kwargs['y']

            if 'id' in passed_kwargs:
                self.id = (passed_kwargs['id'])

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation of a Square
        class
        """
        sqr_args = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

        return sqr_args
