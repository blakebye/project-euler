#!/usr/bin/env python
"""
This module solves Project Euler #3
"""

import math

TEST_VALUE = 600851475143


def factors(value):
    """
    This function returns a high-to-low
    sorted list of all factors of given value.
    """
    list_of_factors = list()
    for potential in range(2, int(math.sqrt(value)) + 1):
        if not value % potential:
            list_of_factors.append(potential)
            list_of_factors.append(value / potential)
    return sorted(set(list_of_factors), reverse=True)


def largest_prime_factor(value):
    """
    This function takes a value, gets all it's factors, and then
    compares them to themselves to determine which of them is
    the highest prime. Often times, factors have similar base factors.
    """
    for factor in factors(value):
        prime = True
        for divisor in factors(value):
            if not factor % divisor and not factor == divisor:
                prime = False
        if prime:
            return factor

print largest_prime_factor(TEST_VALUE)
