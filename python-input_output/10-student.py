#!/usr/bin/python3
"""
module with class
"""


class Student:
    """
    defines a student by first_name, last_name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance;
        if attrs is a list of strings, only attribute names contained
        in this list must be retrieved
        """
        if attrs is None:
            return self.__dict__
        return {key: getattr(self, key) for key
                in attrs if key in self.__dict__}
