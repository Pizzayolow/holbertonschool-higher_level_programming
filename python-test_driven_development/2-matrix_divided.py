#!/usr/bin/python3
"""
divide the datas in a matrix
"""


def matrix_divided(matrix, div):
    """
    look in a matrix and divides by the div
    """
    new_matrix = []
    try:
        for i in range(len(matrix)):
            temp = []
            for element in range(len(matrix[i])):
                result = matrix[i][element] / div
                temp.append(round(result, 2))
            new_matrix.append(temp)
        return(new_matrix)
    except:
        if matrix is not int or float:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if div is not int or float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
