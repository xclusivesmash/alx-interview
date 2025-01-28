#!/usr/bin/python3
"""
module: 0-island_perimeter.
description: calculates the perimeter of an island.
"""


def island_perimeter(grid):
    """ @description.
    Args:
        grid (List[List]]): 2D grid with 0s indicating water and 1s
        representing walls.
    Returns:
        the perimeter of the island
    """
    perimeter = 0
    for i in range(len(grid)):
        # loop through rows.
        for j in range(len(grid[i])):
            # loop through columns.
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    perimeter = perimeter + 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    perimeter = perimeter + 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    perimeter = perimeter + 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    perimeter = perimeter + 1
    return perimeter
