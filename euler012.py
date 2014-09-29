#!/usr/bin/env python
"""
This module solves Project Euler #12
"""

import math


def get_triangle(number):
    """
    This function will return a triangle number. Which
    one will be determined by the input.
    """
    triangle = int(number / 2. * (number + 1))
    return triangle


def prime_factorize(value):
    """
    This function breaks down a value to all of it's prime factors.
    It returns a dictionary with factors as keys and their
    frequency as values. 8 would become {2:3}, 10 {5:1, 2:1}
    The reason for doing this is to help with the Tau function.
    """
    dict_of_primes = dict()
    factored = False
    for main_divisor in xrange(2, int(math.sqrt(value)) + 1):
        if not value % main_divisor and not value == main_divisor:
            factored = True
            dict_of_primes = prime_factorize(main_divisor)
            dict_two = prime_factorize(value / main_divisor)
            for prime in dict_two:
                if prime not in dict_of_primes:
                    dict_of_primes[prime] = dict_two[prime]
                else:
                    dict_of_primes[prime] += dict_two[prime]
            break
    if not factored:
        dict_of_primes[value] = 1
    return dict_of_primes


def total_factors(value):
    """
    This is the Tau function, the divisor function. Any value can have
    it's factors counted by this function. With any prime number, it
    always has two factors. With any non-prime, its factors are equal
    to the product of (every prime * 2)
    """
    total = 1
    primes = prime_factorize(value)
    for number in primes:
        total *= (primes[number] + 1)
    return total


def triangle_divisible_by(number_of_factors):
    """
    Generate all triangle numbers in order until one exceeds the
    given number of factors. This is the solution to the problem.
    """
    counter = int()
    while True:
        counter += 1
        triangle = get_triangle(counter)
        if total_factors(triangle) > number_of_factors:
            return triangle

if __name__ == "__main__":
    TEST_VALUE = 500
    print triangle_divisible_by(TEST_VALUE)
