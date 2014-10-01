#!/usr/bin/env python
"""
This module solves Project Euler #5
"""

import math

TEST_VALUE = 20


def prime_factorize(value):
    """
    This function breaks down a value to all of it's prime factors.
    It returns a dictionary with factors as keys and their
    frequency as values. 8 would become {2:3}, 10 {5:1, 2:1}
    The reason for doing this is to help with the Tau function.
    """
    dict_of_primes = {value: 1}
    for main_divisor in xrange(2, int(math.sqrt(value)) + 1):
        if not value % main_divisor:
            dict_of_primes = prime_factorize(main_divisor)
            dict_two = prime_factorize(value / main_divisor)
            for prime in dict_two:
                if prime not in dict_of_primes:
                    dict_of_primes[prime] = dict_two[prime]
                else:
                    dict_of_primes[prime] += dict_two[prime]
            return dict_of_primes
    return dict_of_primes


def greatest_power(value):
    """
    This function crafts a super-dictionary that lists the max
    power of every prime that needs to go into the solution.
    By multiplying them all together, we find the minimum solution.
    This uses the Tau divisor function idea that if two values
    are coprime their product will share all of their factors.
    """
    total = 1
    high_primes = dict()
    for value in reversed(xrange(value / 2, value)):
        factors_primes = prime_factorize(value)
        for prime in factors_primes:
            if prime not in high_primes:
                high_primes[prime] = factors_primes[prime]
            else:
                high_primes[prime] = max(factors_primes[prime],
                                         high_primes[prime])
    for prime in high_primes:
        total *= (prime ** high_primes[prime])
    return total


def main():
    test_value = 20
    return greatest_power(test_value)

if __name__ == "__main__":
    print main()
