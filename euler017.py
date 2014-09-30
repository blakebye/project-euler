#!/usr/bin/env python
"""
This module solves Project Euler #16
"""

MAP = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
       7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
       12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
       16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
       20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty",
       70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred",
       1000: "thousand"}


def number_to_word(value):
    """
    This function takes a number and writes out the word in english.
    """
    # odd values
    if value <= 20:
        return MAP[value]
    # regular values
    elif value <= 99:
        tens = MAP[(value / 10) * 10]
        ones = MAP[value % 10]
        return tens + ones
    # values from 101-199 have "and"
    elif value % 100:
        if value % 100 <= 20:
            hundreds = MAP[(value / 100) % 10] + MAP[100] + "and"
            return hundreds + MAP[value % 100]
        else:
            hundreds = MAP[(value / 100) % 10] + MAP[100] + "and"
            tens = MAP[(value % 100 / 10) * 10]
            ones = MAP[value % 100 % 10]
            return hundreds + tens + ones
    # 100, 200, 300
    elif value % 1000:
        return MAP[value / 100] + MAP[100]
    # 1000
    else:
        return MAP[value / 1000] + MAP[1000]


def letter_count(value):
    """
    This function counts the letters in a number.
    """
    return len(number_to_word(value))


def letter_count_to_a_point(max_value):
    """
    This function counts the letters in every number
    up to a maximum value and sums them together
    """
    total = int()
    for value in xrange(1, max_value + 1):
        total += letter_count(value)
    return total


def main():
    """
    Solves the problem.
    """
    test_value = 1000
    return letter_count_to_a_point(test_value)

if __name__ == "__main__":
    print main()
