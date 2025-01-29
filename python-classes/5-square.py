#!/usr/bin/python3
"""
In this module we are going to create a class called square,
to create the class we use class and then to indicate its size
as an attribute we use __init__: and to make it private we use
self.__size with raises and return square
"""


class Square:
    """
    class Square that defines a square
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        for e in range(self.__size):
            print("#" * self.__size)
