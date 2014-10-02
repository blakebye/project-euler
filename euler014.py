#!/usr/bin/env python
"""
This module solves Project Euler #14
"""


def collatz(start, terms):
    term_count = int()
    new_terms = dict()
    value = start
    while value not in terms:
        if not value % 2:
            value /= 2
        else:
            value = value * 3 + 1
        if value in terms:
            break
        term_count += 1
        new_terms[value] = term_count
    term_count += terms[value]
    terms[start] = term_count
    for new_term in new_terms:
        terms[new_term] = term_count - new_terms[new_term]
    return (term_count, terms)

def max_collatz(high_point):
    terms = {1: 1}
    longest_chain = int()
    highest_starter = int()
    low_point = high_point / 2
    if not low_point % 2:
        low_point += 1
    for start in xrange(low_point, high_point, 2):
        if start in terms:
            term_count = terms[start]
        else:
            term_count, terms = collatz(start, terms)
        if term_count > longest_chain:
            longest_chain = term_count
            highest_starter = start
    return highest_starter


def main():
    test_value = 1000000
    return max_collatz(test_value)

if __name__ == "__main__":
    print main()
