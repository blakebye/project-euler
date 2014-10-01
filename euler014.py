#!/usr/bin/env python
"""
This module solves Project Euler #14
"""


def collatz(start, terms):
    if start in terms:
        return terms[start], terms
    value = start
    term_count = 1
    if not value % 2:
        value /= 2
    else:
        value = value * 3 + 1
    if value in terms:
        terms[start] = terms[value] + 1
        return terms[value], terms
    next = collatz(value, terms)
    if value in terms:
        terms[start] = terms[value] + 1
        return terms[value], terms
    term_count += next[0]
    terms.update(next[1])
    terms[start] = term_count
    return (term_count, terms)

def max_collatz(high_start):
    terms = {1: 1}
    longest_chain = int()
    highest_starter = int()
    for start in xrange(high_start / 2, high_start):
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
