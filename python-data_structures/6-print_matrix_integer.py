#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in range(len(row)):
            if element < len(row) - 1:
                print("{:d}".format(row[element]), end=" ")
            else:
                print("{:d}".format(row[element]))
          
