#!/usr/bin/python3
"""
Module with the method is_same_class.

"""


def is_same_class(obj, a_class):
    """Returns True if the object is instance of specified class."""

    return type(obj) is a_class
