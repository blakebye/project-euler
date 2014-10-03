#!/usr/bin/env python
"""
This module solves Project Euler #21
"""

import math


def sum_of_proper_divisors(value):
    """
    This function returns the sum of all divisors from 1 - n / 2
    """
    divisors = list()
    for possible_factor in xrange(2, int(math.sqrt(value)) + 1):
        if not value % possible_factor:
            divisors += [possible_factor, value / possible_factor]
    divisors.append(1)
    return sum(sorted(list(set(divisors))))


def sum_of_amiables(max_value):
    """
    This function takes a value and returns the sum of all
    the amiable numbers up to that point.
    """
    list_of_sums = []
    amiables = []
    for value in xrange(max_value + 1):
        list_of_sums.append(sum_of_proper_divisors(value))
    for value in xrange(max_value + 1):
        try:
            if (list_of_sums[value] != value and 
                value == list_of_sums[list_of_sums[value]]):
                amiables += [value, list_of_sums[value]]
        except:
            pass
    amiables = list(set(amiables))
    return sum(amiables)


def main():
    """
    Solves the problem
    """
    test_value = 10000
    return sum_of_amiables(test_value)

if __name__ == "__main__":
    print main()
