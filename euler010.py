#!/usr/bin/env python
"""
This module solves Project Euler #10
"""

import math


def generate_primes(max_value):
    """
    This function takes a value and returns a list of
    all primes up to that value.
    """
    primality = [False] * 2 + [True] * (max_value - 2)
    # prime_list = list()
    for non_prime in xrange(4, max_value, 2):
        primality[non_prime] = False
    for factor in xrange(3, int(math.sqrt(len(primality)) + 1), 2):
        if primality[factor]:
            for non_prime in xrange(factor ** 2, max_value, factor * 2):
                primality[non_prime] = False
    return primality


def sum_of_primes(max_value):
    """
    This function takes a value and gives the sum
    of all primes below that number.
    """
    total = int()
    primality = generate_primes(max_value)
    for number, prime in enumerate(primality):
        if prime:
            total += number
    return total


def main():
    """
    Solves the problem.
    """
    test_value = 2000000
    return sum_of_primes(test_value)

if __name__ == "__main__":
    print main()
