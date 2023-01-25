#!/usr/bin/python3
"""
Module for 0x1F. Pascal's Triangle.
Holberton School
Specializations - Interview Preparation ― Algorithms
"""


def pascal_triangle(n):
    """
    Returns the representation of the Pascal’s triangle of `n`
    """
    if n <= 0:
        return []

    pascal = [[1 for x in range(y)] for y in range(1, n + 1)]

    for x in range(2, n):
        for y in range(1, len(pascal[x]) - 1):
            pascal[x][y] = pascal[x - 1][y - 1] + pascal[x - 1][y]

    return 