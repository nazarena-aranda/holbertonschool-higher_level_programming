#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best = 0
    key = None
    for k, v in a_dictionary.items():
        if v > best:
            best = v
            key = k
    return key
