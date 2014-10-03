#!/usr/bin/env python
"""
This module solves Project Euler #25
"""


def first_fib_term(digits):
    """
    This function generates fibonacci terms and also counts which
    term it is, until it hits the number of digits in the input.
    """
    count = int()
    term_one, term_two = 0, 1
    while True:
        term_one, term_two = term_two, term_one + term_two
        count += 1
        if term_one > 10 ** (digits - 1):
            return count


def main():
    """
    Solves the problem
    """
    test_value = 1000
    return first_fib_term(test_value)

if __name__ == "__main__":
    print main()
