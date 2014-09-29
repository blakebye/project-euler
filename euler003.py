#!/usr/bin/env python
"""
This module solves Project Euler #3
"""

import math


def factors(value):
    """
    This function returns a high-to-low
    sorted list of all factors of given value.
    """
    possibles = xrange(2, int(math.sqrt(value)) + 1)
    list_of_factors = [a for b in ((factor, value / factor) for
                       factor in possibles if not value % factor) for a in b]
    return sorted(set(list_of_factors), reverse=True)


def largest_prime_factor(value):
    """
    This function takes a value, gets all it's factors, and then
    compares them to themselves to determine which of them is
    the highest prime. Often times, factors have similar base factors.
    """
    list_of_factors = factors(value)
    for factor in list_of_factors:
        prime = True
        for divisor in list_of_factors:
            if not factor % divisor and not factor == divisor:
                prime = False
        if prime:
            return factor


def main():
    """
    Solves problem.
    """
    test_value = 600851475143
    print largest_prime_factor(test_value)

if __name__ == "__main__":
    main()
