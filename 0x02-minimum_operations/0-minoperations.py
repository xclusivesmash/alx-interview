#!/usr/bin/python3
"""
module: 0-minoperations
description: returns minimum #operations
"""


def minOperations(n):
    """minOperations
    """
    if (n < 2):
        return 0
    operations, root = 0, 2
    while root <= n:
        if n % root == 0:
            # total even-divisions by root = total operations
            operations += root
            n = n / root
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return operations
