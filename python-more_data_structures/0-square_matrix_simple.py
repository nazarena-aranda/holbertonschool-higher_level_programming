#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return list(map(lambda row: [e * e for e in row], matrix))