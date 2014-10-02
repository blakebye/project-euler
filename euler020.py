#!/usr/bin/env python
"""
This module solves Project Euler #20
"""

import math


def sum_of_factorial_digits(number):
    """
    This function takes a number, finds its factorial,
    and sums the digits of that factorial.
    """
    total = int()
    for char in str(math.factorial(number)):
        total += int(char)
    return total


def main():
    """
    Solves the problem
    """
    test_value = 100
    return sum_of_factorial_digits(test_value)

if __name__ == "__main__":
    print main()
