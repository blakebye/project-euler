#!/usr/bin/env python
"""
This module solves Project Euler #23
"""

import math

def is_abundant(value):
    """
    This function returns if value is abundant or not
    """
    divisors = list()
    for possible_factor in xrange(2, int(math.sqrt(value)) + 1):
        if not value % possible_factor:
            divisors += [possible_factor, value / possible_factor]
    divisors.append(1)
    return sum(set(divisors)) > value


def create_sums(abundants, max_value):
    """
    This function takes all abundant numbers up to the max and generates
    a dictionary of all of their sums
    """
    sums = dict()
    for one_index, value_one in enumerate(abundants):
        for value_two in abundants[one_index:]:
            if value_one + value_two <= max_value:
                sums[value_one + value_two] = True
    return sums

def checker(sums, max_value):
    total = int()
    for possible in xrange(1, max_value):
        if not sums.get(possible, False):
            total += possible
    return total

def find_non_sums(max_value):
    abundants = list()
    for value in xrange(1, max_value + 1):
        if is_abundant(value):
            abundants.append(value)
    sums = create_sums(abundants, max_value)
    total = checker(sums, max_value)
    return total

def main():
    test_value = 28123
    return find_non_sums(test_value)

if __name__ == "__main__":
    print main()
