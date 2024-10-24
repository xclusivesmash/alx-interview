#!/usr/bin/python3
"""
Module: 0-pascal_triangle
Description: Solves Pascal's triangle.
"""


def pascal_triangle(n):
    """solves Pascal's triangle."""
    if n <= 0:
        return []
    store = []
    for x in range(1, n + 1):
        tmp = []
        one = 1
        for xx in range(1, x + 1):
            tmp.append(one)
            one = one * (x - xx) // xx
        store.append(tmp)
    return store
