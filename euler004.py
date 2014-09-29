#!/usr/bin/env python
"""
This module solves Project Euler #4
"""


def is_palindrome(value):
    """
    This function takes a value and
    returns if it's a palindrome or not.
    """
    for digit in range(len(str(value)) / 2):
        if str(value)[digit] != str(value)[-digit - 1]:
            return False
    return True


def largest_palindromic_product(digits):
    """
    This function takes every product up to the number of specified
    digits and returns the highest palindromic product there was.
    """
    max_factor = 10 ** digits
    max_palindromic_product = int()
    for i in range(max_factor, 1, -1):
        for j in range(990, 0, -11):
            if is_palindrome(i * j):
                max_palindromic_product = max(max_palindromic_product, i * j)
                break
    return max_palindromic_product


def main():
    test_value = 3
    print largest_palindromic_product(test_value)

if __name__ == "__main__":
    main()
