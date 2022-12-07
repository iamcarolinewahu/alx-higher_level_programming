#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    New_matrix = []
    i = 0
    for x in matrix:
        New_matrix.append([])
        for y in matrix[i]:
            New_matrix[i].append(y**2)
        i += 1

    return New_matrix
