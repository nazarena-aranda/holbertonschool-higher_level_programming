#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str):
        return 0

    ref = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'D': 500, 'L': 50, 'M': 1000}
    num = 0
    prev = 0

    for rn in reversed(roman_string):
        n = ref[rn]
        if prev > n:
            num -= n
        else:
            num += n
        prev = n
    return num
