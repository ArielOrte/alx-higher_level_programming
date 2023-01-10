#!/usr/bin/python3
"""

Module with the class Student.

"""


class Student:
    """Class with methods to_json for retrieves dictionary."""

    def __init__(self, first_name, last_name, age):
        """Method for initialized all atributes.

        Args:
            first_name (str): first name of the perimeter.
            last_name (str): last name of the paremeter.
            age (int): value of age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary representation
        of a Student instance."""

        return self.__dict__
