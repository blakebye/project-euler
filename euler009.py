#!/usr/bin/env python
"""
This module solves Project Euler #9
"""

TEST_VALUE = 1000


def is_triplet(side_one, side_two, side_three):
    """
    This function takes three values and returns whether or not
    they would make a perfect triangle. int ^ 2 + int ^ 2 = int ^ 2
    """
    side_one, side_two, side_three = sorted((side_one, side_two, side_three))
    return side_one ** 2 + side_two ** 2 == side_three ** 2


def triplet_product(value):
    """
    This function takes a sum and finds the perfect triangle sides
    that add up to make that sum. It then returns their product.
    """
    for side_one in range(2, value / 2):
        for side_two in range((value / 2) - side_one, value / 2):
            if is_triplet(side_one, side_two, value - side_one - side_two):
                return side_one * side_two * (value - side_one - side_two)

print triplet_product(TEST_VALUE)
