#!/usr/bin/env python
"""
This module solves Project Euler #7
"""

import math


def generate_prime(value, efficiency):
    """
    This function takes a value and tries to find that prime.
    It uses the prime number theorem to overshot an estimate
    of the prime and then tests up to that overshot.
    """
    prime_list = [2]
    estimate = int(efficiency * value * math.log(value))
    primality = [False] * 2 + [True] * (estimate - 2)
    for non_prime in xrange(4, estimate, 2):
        primality[non_prime] = False
    for factor in xrange(3, int(math.sqrt(len(primality)) + 1), 2):
        if primality[factor]:
            for non_prime in xrange(factor ** 2, estimate, factor * 2):
                primality[non_prime] = False
    for number, prime in enumerate(primality):
        if prime:
            prime_list.append(number)
    return prime_list[value]


def main():
    """
    Solves the problem.
    """
    test_value = 10001
    # 1.15 is cutting it close, only works for value > 2000
    # 2.5 is safe for all values
    if test_value < 2000:
        efficiency_coefficient = 2.5
    else:
        efficiency_coefficient = 1.15
    return generate_prime(test_value, efficiency_coefficient)

if __name__ == "__main__":
    print main()
