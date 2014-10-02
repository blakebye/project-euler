#!/usr/bin/env python
"""
This module solves Project Euler #15
"""


def number_of_routes(rows, columns):
    """
    This function takes a number of rows and columns and
    returns how many routes there would be if each
    intersection allows for 2 paths except those on the edges
    """
    grid = [[0 for x in xrange(columns + 1)] for x in xrange(rows + 1)]
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if i == 0:
                grid[i][j] = 1
            elif j == 0:
                grid[i][j] = 1
            else:
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[rows][columns]

def main():
    """
    Solves the problem.
    """
    return number_of_routes(20, 20)

if __name__ == "__main__":
    print main()
