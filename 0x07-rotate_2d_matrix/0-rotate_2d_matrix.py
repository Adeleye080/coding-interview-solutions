#!/usr/bin/python3
""" ALX interview. """


def rotate_2d_matrix(matrix):
    """ Rotate a matrix 90 degrees clockwise. """
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for item in range(len(matrix)):
        matrix[item] = matrix[item][::-1]
    return matrix
