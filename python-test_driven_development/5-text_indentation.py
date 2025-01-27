#!/usr/bin/python3
"""
In this module prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in [".", "?", ":"]:
            result = result.strip()
            result += "\n\n"

    print(result.strip())
