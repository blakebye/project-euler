#!/usr/bin/env python
"""
This module solves Project Euler #9
"""


def generate_triplet_product(max_value):
    for n in xrange(1, max_value / 2):
        for m in xrange(n + 1, max_value):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2
            if a + b + c == 1000:
                return a * b * c


def main():
    """
    Solves the problem.
    """
    test_value = 1000
    return generate_triplet_product(test_value)

if __name__ == "__main__":
    print main()
