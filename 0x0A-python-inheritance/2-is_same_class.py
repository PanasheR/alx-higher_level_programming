#!/usr/bin/python3


"""
This is an example of the is_same_class function
>>> a = 1
>>> if is_same_class(a, int):
... print("{} is an instance of the class {}".format(a, int.__name__))
>>> if is_same_class(a, float):
... print("{} is an instance of the class {}".format(a, float.__name__))
>>> if is_same_class(a, object):
... print("{} is an instance of the class {}".format(a, object.__name__))
1 is an instance of the class int
"""


def is_same_class(obj, a_class):
    """
    This function that returns True if the object is exactly an instance of the
    specified class ; otherwise False
    """
    if type(obj) is a_class:
        return True

    else:
        return False
