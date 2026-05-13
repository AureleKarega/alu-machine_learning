#!/usr/bin/env python3
"""Adds two 2D matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """Returns a new matrix with added elements"""

    # Check if matrices have the same shape
    if len(mat1) != len(mat2):
        return None

    for row1, row2 in zip(mat1, mat2):
        if len(row1) != len(row2):
            return None

    # Add matrices element-wise
    return [
        [mat1[i][j] + mat2[i][j] for j in range(len(mat1[i]))]
        for i in range(len(mat1))
    ]
