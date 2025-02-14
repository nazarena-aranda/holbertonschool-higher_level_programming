#!/usr/bin/python3
"""
module with function
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
