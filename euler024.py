#!/usr/bin/env python
"""
This module solves Project Euler #24
"""

from itertools import islice, permutations


def get_permutation(digits, which):
    """
    This function takes a list of digits and a number
    and returns that specific number's permutation in
    lexicographic order.
    """
    perms = permutations(digits)
    perm = islice(perms, which - 1, which).next()
    return "".join([str(x) for x in perm])


def main():
    """
    Solves the problem.
    """
    test_digits = range(10)
    test_value = 1000000
    return get_permutation(test_digits, test_value)


if __name__ == "__main__":
    print main()
