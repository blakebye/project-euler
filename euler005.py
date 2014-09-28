#!/usr/bin/env python
"""
This module solves Project Euler #5
"""

TEST_VALUE = 20


def check_divisibility(max_value):
    """
    This function takes max_value and finds the lowest number that is
    divisible by every single value from one to max_value.
    """
    found = False
    guess = int()
    divisors = list(reversed(range(max_value / 2, max_value)))
    while not found:
        guess += max_value
        for divisor in divisors:
            if guess % divisor:
                break
            if divisor == max_value / 2:
                found = True
    print guess

check_divisibility(TEST_VALUE)
