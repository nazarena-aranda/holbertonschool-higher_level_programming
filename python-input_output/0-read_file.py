#!/usr/bin/python3
"""
module with function
"""


def read_file(filename=""):
    """
    function that reads a text file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
