#!/usr/bin/env python
"""
This module solves Project Euler #10
"""

TEST_VALUE = 2000000


def generate_primes(max_value):
    """
    This function takes a value and returns a list of
    all primes up to that value.
    """
    primality = [False] * 2 + [True] * (max_value - 2)
    # prime_list = list()
    for non_prime in range(4, max_value, 2):
        primality[non_prime] = False
    for factor in range(3, len(primality), 2):
        if primality[factor]:
            # prime_list.append(factor)
            for non_prime in range(factor ** 2, max_value, factor * 2):
                primality[non_prime] = False
    return primality


def sum_of_primes(max_value):
    """
    This function takes a value and gives the sum
    of all primes below that number.
    """
    total = int()
    primality = generate_primes(max_value)
    for number in range(len(primality)):
        if primality[number]:
            total += number
    return total

print sum_of_primes(TEST_VALUE)
