#!/usr/bin/env python
"""
This module solves Project Euler #16
"""

def power_digit_sum(exponent):
    """
    This function takes a value, exponentiates 2 by that value,
    and adds up all the digits in the total.
    """
    value = 2 ** exponent
    sum = int()
    for x in str(value):
        sum += int(x)
    return sum

def main():
    """
    Solves the problem.
    """
    test_value = 1000
    return power_digit_sum(test_value)

if __name__ == "__main__":
    print main()
