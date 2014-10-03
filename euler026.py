#!/usr/bin/env python
"""
This module solves Project Euler #26
"""

from decimal import *

def cycle_repeat_count(highest_denominator):
    longest_cycle = (0, 0)
    for denom in xrange(2, highest_denominator):
        cycle = list()
        remainder = 10 % denom
        while remainder and remainder not in cycle:
            cycle.append(remainder)
            remainder = (remainder * 10) % denom
        if len(cycle) > longest_cycle[1]:
            longest_cycle = (denom, len(cycle))
    return longest_cycle[0]



def main():
    test_value = 1000
    return cycle_repeat_count(test_value)

if __name__ == "__main__":
    print main()
