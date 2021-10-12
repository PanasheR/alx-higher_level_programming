#!/usr/bin/python3


"""This is an example of the append_after function
>>> append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
At Holberton School,
Python is really important,
But it can be very hard if:
- You don't get all Pythonic tricks
- You don't have strong C knowledge.


cat append_after_100.txt

Python is really important,
"C is fun!"
But it can be very hard if:
- You don't get all Pythonic tricks
"C is fun!"
- You don't have strong C knowledge.
"""


def append_after(filename="", search_string="", new_string=""):

    """
    Function that inserts a line of text to a file, after each line containing
    a specific string
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        f. close()

    with open(filename, mode='w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

        f.close()
