#!/usr/bin/python3

def roman_to_int(roman_string):

    ref = {'I': 1, 'V': 5, 'X': 10, 'C': 100, 'D': 500, 'L': 50, 'M': 1000}
    num = 0
    prev = 0
    
    if not roman_string:
        return 0
    for rn in reversed(roman_string):
        n = ref[rn]
        if prev > n:
            num -= n
        else:
            num += n
        prev = n
    return num
