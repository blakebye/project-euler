#!/usr/bin/env python
"""
This module solves Project Euler #1
"""

TEST_VALUE = 1000


def sum_of_multiples(max_value):
    """
    This function returns the sum of all digits divisible by 3 or 5
    up to a maximum of the function's only input, max_value.
    """
    total = int()
    for value in range(max_value):
        if (not value % 3) or (not value % 5):
            total += value
    return total

print sum_of_multiples(TEST_VALUE)
