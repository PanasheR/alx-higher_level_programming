#!/usr/bin/python3


"""
This is an example of the inherits_from function
>>> inherits_from = __import__('4-inherits_from').inherits_from
>>> a = True
>>> if inherits_from(a, int):
...    print("{} inherited from class {}".format(a, int.__name__))
>>> if inherits_from(a, bool):
...    print("{} inherited from class {}".format(a, bool.__name__))
>>> if inherits_from(a, object):
...    print("{} inherited from class {}".format(a, object.__name__))
True inherited from class int
True inherited from class object
"""


def inherits_from(obj, a_class):
    """
    This is a function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified class ;
    otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True

    else:
        return False
