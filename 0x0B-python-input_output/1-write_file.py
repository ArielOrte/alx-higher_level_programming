#!/usr/bin/python3
"""

Module with write_file.

"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file and return the number
    of characters written."""

    with open(filename, 'w') as f:
        return f.write(text)
