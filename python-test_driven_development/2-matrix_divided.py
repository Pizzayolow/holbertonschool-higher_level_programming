#!/usr/bin/python3

def matrix_divided(matrix, div):
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
