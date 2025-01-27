#!/usr/bin/python3
"""
Module to find the max integer in a list
"""


def max_integer(lst=[]):
    """
    Function to find and return the max integer
    in a list of integers
    """
    if not isinstance(lst, list):
        raise TypeError("The argument must be a list")
    
    if len(lst) == 0:
        return None

    result = lst[0]
    i = 1
    while i < len(lst):
        if lst[i] > result:
            result = lst[i]
        i += 1
    return result
