#!/usr/bin/env python
"""
This module solves Project Euler #6
"""


def sum_of_squares(max_value):
    """
    This function gives the sum of
    (all the squares up to max_value)
    """
    total = int()
    for i in xrange(max_value + 1):
        total += i ** 2
    return total


def square_of_sum(max_value):
    """
    This function gives the square of
    (the sum of all values up to max_value)
    """
    total = int()
    for i in xrange(max_value + 1):
        total += i
    return total ** 2


def difference(value):
    """
    This function gives the difference between the
    square of the sum and the sum of the squares.
    """
    return square_of_sum(value) - sum_of_squares(value)


def main():
    """
    Solves the problem.
    """
    test_value = 100
    return difference(test_value)

if __name__ == "__main__":
    main()
