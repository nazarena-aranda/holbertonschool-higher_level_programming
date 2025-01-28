#!/usr/bin/python3
"""
In this module we are going to create a class called square,
to create the class we use class and then to indicate its size
as an attribute we use __init__: and to make it private we use
self.__size
"""


class Square:
    """
    class Square that defines a square
    """
    def __init__(self, size):
        self.__size = size
