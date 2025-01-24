#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maximum = my_list[0]

    for e in my_list:
        if e > maximum:
            maximum = e
    return maximum
