#!/usr/bin/python3
"""

Module with class Rectangle.

"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits out of BaseGeometry.
    
    Attributes:
            width  {int} -- [Rectangle's width]
            height {int} -- [Rectangle's height]
    """

    def __init__(self, width, height):
        """
        private attributes width and height,
        and validating if they are ints.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
