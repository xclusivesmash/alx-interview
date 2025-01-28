#!/usr/bin/python3
"""
module: 0-rotate_2d_matrix
description: interview questions regarding rotating a 2D matrix.
"""


def rotate_2d_matrix(matrix):
    """ @description: rotation -> 90 deg. clockwise.
    Args:
        matrix (list[list]): a 2D matrix
    """
    length = len(matrix)
    for i in range(int(length / 2)):
        y = (length - i - 1)
        for j in range(i, y):
            x = (length - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            # final rotation.
            matrix[j][y] = tmp
