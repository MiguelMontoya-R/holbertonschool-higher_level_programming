#!/usr/bin/python3
""" Function to divide a matrix
"""


def matrix_divided(matrix, div):
    """ Divide a matrix

    Arguments:
        matrix {int} -- The matrix to be divided
        div {[type]} -- number that is going to divide the matrix

    Return:
        The new matrix qith the elements divided
    """
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    elif not matrix:
        raise TypeError('matrix must be a matrix (list of lists) of\
 integers/floats')
    elif len(matrix) == 1:
        raise TypeError('matrix must be a matrix (list of lists) of\
 integers/floats')
    new_matrix = []
    mega_new_matrix = []
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError('Each row of the matrix must have the same size')
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of\
 integers/floats')
            else:
                pass
            result = element / div
            new_matrix.append(round(result, 2))
        mega_new_matrix.append(new_matrix)
        new_matrix = []
    return mega_new_matrix
