#!/usr/bin/env python3
"""Concatenates two numpy matrices along a given axis"""


import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Returns a concatenated numpy array"""
    return np.concatenate((mat1, mat2), axis=axis)
