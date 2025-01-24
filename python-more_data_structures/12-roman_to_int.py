#!/usr/bin/python3

def roman_to_int(roman_string):

    ref = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'D': 500, 'L': 50, 'M': 1000}
    num = 0
    prev = None

    for rn in roman_string:
        if prev is not None:
            if ref[prev] < ref[rn]:
                num += ref[rn] - ref[prev]
            else:
                num += ref[rn]
        elif rn == roman_string[0]:
            num += ref[rn]
            prev = rn
    return num
