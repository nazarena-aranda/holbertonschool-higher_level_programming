#!/usr/bin/python3
"""
create a class MyList
"""


class MyList(list):
    """
    create a function that order a lists
    """
    def print_sorted(self):
        print(sorted(self))