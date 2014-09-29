#!/usr/bin/env python
"""
This module solves Project Euler #2
"""


def gen_fib(max_value):
    """
    This function returns a list of all the numbers of a
    fibonacci sequence that do not exceed max_value.
    """
    term_one = 1
    term_two = 2
    fib = [term_one, term_two]
    while term_one + term_two <= max_value:
        fib.append(term_one + term_two)
        term_one, term_two = term_two, term_one + term_two
    return fib


def sum_of_even_fib(max_value):
    """
    This function returns the sum of all even numbers of a
    fibonacci sequense that do not exceed max_value.
    """
    total = int()
    for fib_term in gen_fib(max_value):
        if not fib_term % 2:
            total += fib_term
    return total


def main():
    """
    Solves problem.
    """
    test_value = 4000000
    print sum_of_even_fib(test_value)

if __name__ == "__main__":
    main()
