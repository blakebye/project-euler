#!/usr/bin/env python
"""
This module solves Project Euler #7
"""

import math

TEST_VALUE = 10001

# 1.15 is cutting it close, only works for > 2000
# 2.5 is safe for everything
EFFICIENCY_COEFFICIENT = 1.15

if TEST_VALUE < 2000:
    EFFICIENCY_COEFFICIENT = 2.5


def generate_prime(value):
    """
    This function takes a value and tries to find that prime.
    It uses the prime number theorem to overshot an estimate
    of the prime and then tests up to that overshot.
    """
    estimate = int(EFFICIENCY_COEFFICIENT * value * math.log(value))
    primality = [False] * 2 + [True] * estimate
    prime_list = list()
    for factor in range(len(primality)):
        if primality[factor]:
            prime_list.append(factor)
            for non_prime in range(factor ** 2, estimate, factor):
                primality[non_prime] = False
    return prime_list[value - 1]

print generate_prime(TEST_VALUE)
