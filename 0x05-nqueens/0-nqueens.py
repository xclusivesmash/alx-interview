#!/usr/bin/python3
"""
module: 0-nqueens
description: solves the nqueens challenge.
"""
import sys


# checks for correct usage
if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

# checks data types used
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

# checks for limit
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, i=0, a=[], b=[], c=[]):
    """Locate the viable positions.
    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """solve for the nqueens
    """
    k = []
    i = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([i, s])
            i = i + 1
        print(k)
        k = []
        i = 0


solve(n)
