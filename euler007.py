#!/usr/bin/env python
"""
This module solves Project Euler #7
"""

import math

TEST_VALUE = 10001

# 1.15 is cutting it close, only works for value > 2000
# 2.5 is safe for all values
if TEST_VALUE < 2000:
    EFFICIENCY_COEFFICIENT = 2.5
else:
    EFFICIENCY_COEFFICIENT = 1.15


def generate_prime(value):
    """
    This function takes a value and tries to find that prime.
    It uses the prime number theorem to overshot an estimate
    of the prime and then tests up to that overshot.
    """
    prime_list = list()
    estimate = int(EFFICIENCY_COEFFICIENT * value * math.log(value))
    primality = [False] * 2 + [True] * (estimate - 2)
    for non_prime in range(4, estimate, 2):
                primality[non_prime] = False
    for factor in range(len(primality)):
        if primality[factor]:
            prime_list.append(factor)
            for non_prime in range(factor ** 2, estimate, factor * 2):
                primality[non_prime] = False
    return prime_list[value - 1]

print generate_prime(TEST_VALUE)
