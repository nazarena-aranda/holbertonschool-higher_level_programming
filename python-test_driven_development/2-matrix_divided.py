#!/usr/bin/python3
"""
This module divides a matrix, for this we create a new matrix and
we divide it by div and save the result in that matrix.
"""

def matrix_divided(matrix, div):
    """
    This function divides the numbers of a matrix by div.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for i in range(len(row)):
            res = row[i] / div
            new_row.append(round(res, 2))
        new_matrix.append(new_row)

    return new_matrix
