#!/usr/bin/python3


"""
This is an example of the is_kind_of_class function
>>> a = 1
>>> if is_kind_of_class(a, int):
...    print("{} comes from {}".format(a, int.__name__))
>>> if is_kind_of_class(a, float):
...    print("{} comes from {}".format(a, float.__name__))
>>> if is_kind_of_class(a, object):
...    print("{} comes from {}".format(a, object.__name__))
1 comes from int
1 comes from object
"""


def is_kind_of_class(obj, a_class):
    """
    This function eturns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class ;
    otherwise False.
    """
    if isinstance(obj, a_class):
        return True

    else:
        return False
