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


def triangle_divisible_by(value):
    """
    This function goes through every triangle number, and uses another
    trick of the tau function to more quickly determine how many
    factors a specific value has.
    """
    triangle_number = int()
    divisors = int()
    while divisors <= value:
        triangle_number += 1
        if not triangle_number % 2:
            f_1 = total_factors(triangle_number / 2)
            f_2 = total_factors(triangle_number + 1)
        else:
            f_1 = total_factors((triangle_number + 1) / 2)
            f_2 = total_factors(triangle_number)
        divisors = f_1 * f_2
    triangle = int(triangle_number / 2. * (triangle_number + 1))
    return triangle

if __name__ == "__main__":
    TEST_VALUE = 500
    print triangle_divisible_by(TEST_VALUE)
