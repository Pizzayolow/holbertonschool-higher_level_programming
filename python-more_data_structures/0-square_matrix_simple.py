#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_squared = []
    for i in range(len(matrix)):
        matrix_squared.append(list(map(lambda x: x ** 2, matrix[i])))
    return(matrix_squared)
