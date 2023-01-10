#!/usr/bin/python3
"""

Module with append_write.

"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file and return
    the number of characters added."""

    with open(filename, 'a') as f:
        return f.write(text)
