#!/usr/bin/python3
"""
Module with class Rectangle.

"""

class Rectangle(BaseGeometry):
    """Rectangle class that inherits out of BaseGeometry."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
