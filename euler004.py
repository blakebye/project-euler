#!/usr/bin/env python
"""
This module solves Project Euler #4
"""


def divisible_by_x_digits(number, digits):
    for factor_one in xrange(10 ** digits - 1, 1, -1):
        for factor_two in xrange(10 ** digits - 1, 1, -1):
            if factor_one * factor_two == number:
                return True
            if factor_one * factor_two < number:
                break


def max_palindrome(digits):
    """
    This function takes a number of digits and starts generating the
    maximum possible palindromes. Then it checks one at a time if
    those are divisible by two 3-digit numbers and returns the first that is.
    """
    list_of_palindromes = list()
    max_value = (10 ** digits - 1) ** 2
    if digits % 2:
        max_value -= 4
    for number in xrange(max_value, 1, -11):
        palindrome = True
        for char in xrange(len(str(number)) / 2):
            if str(number)[char] != str(number)[-char - 1]:
                palindrome = False
                break
        if palindrome and divisible_by_x_digits(number, digits):
            return number


def main():
    test_value = 3
    print max_palindrome(test_value)

if __name__ == "__main__":
    main()
