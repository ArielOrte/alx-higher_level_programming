#!/usr/bin/python3
"""

Module with read_file.

"""


def read_file(filename=""):
    """Function that reads a text file and prints it."""

    with open(filename) as f:
        text = f.read()
        print(text, end="")
