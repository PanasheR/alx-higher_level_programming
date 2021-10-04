#!/usr/bin/python3


"""
This is an example of the say_my_name function.
>>> say_my_name("Panashe", "Rusakaniko")
Panashe Rusakaniko
"""


def say_my_name(first_name, last_name=""):
    """This function prints 2 strings"""

    if isinstance(first_name, str) is False:
        raise TypeError('first_name must be a string')

    elif isinstance(last_name, str) is False:
        raise TypeError('last_name must be a string')

    else:
        print('My name is {} {}'.format(first_name, last_name))
