#!/usr/bin/env python3
"""Function that calculates the shape of a matrix"""


def matrix_shape(matrix):
    """Returns the shape of a matrix as a list of integers"""
    shape = []
    current = matrix
    while isinstance(current, list):
        shape.append(len(current))
        current = current[0]
    return shape
