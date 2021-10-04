#!/usr/bin/python3


"""
This is an example of the add_integer function.
>>> add_integer(1, 20)
21
"""


def add_integer(a, b=98):
    """
    This function adds 2 integers and returns the sum
    """

    if ((type(a) is not float and type(a) is not int) or a != a or
            a == float('inf') or a == -float('inf')):
        raise TypeError('a must be an integer')

    if ((type(b) is not float and type(b) is not int) or b != b or
            b == float('inf') or b == -float('inf')):
        raise TypeError('b must be an integer')

    x = int(a)
    y = int(b)

    return (x + y)
