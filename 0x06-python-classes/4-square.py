#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """__init__ Initialize a new Square.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
