#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integer"""
    if not matrix:
        return
    for row in matrix:
        for i, col in enumerate(row):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(col), end="")
        print()
   