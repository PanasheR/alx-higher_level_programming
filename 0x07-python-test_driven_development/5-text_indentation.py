#!/usr/bin/python3


"""
This is an example of the text_indentation function.
>>> text_indentation("Hi! How are you?")
Hi!
How are you?
"""


def text_indentation(text):
    """
    This function parses text with 2 new lines after reading
    '?, '.', and ':'
    """
    special = ['?', '.', ':']

    if type(text) is not str:
        raise TypeError('text must be a string')

    x = 0

    while x < len(text):
        if x+1 == len(text):
            print('{}'.format(text[x]), end='')
            break

        if text[x] in special and text[x+1] == ' ':
            print('{}'.format(text[x]), end='\n\n')
            y = 1
            while text[x+y] == ' ' and x+y != len(text):
                y += 1
            x += y
            continue

        if text[x] in special and text[x+1] != ' ':
            print('{}'.format(text[x]), end='\n\n')
            x += 1
            continue

        print('{}'.format(text[x]), end='')

        x += 1
