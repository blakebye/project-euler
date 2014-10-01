#!/usr/bin/env python
"""
This module solves Project Euler #19
"""

from datetime import date, timedelta

ONE_DAY = timedelta(days=1)
ONE_WEEK = timedelta(days=7)
TWO_WEEKS = timedelta(days=14)
THREE_WEEKS = timedelta(days=21)
FOUR_WEEKS = timedelta(days=28)
FIVE_WEEKS = timedelta(days=35)
SIX_WEEKS = timedelta(days=42)
SEVEN_WEEKS = timedelta(days=49)
EIGHT_WEEKS = timedelta(days=56)
NINE_WEEKS = timedelta(days=63)


def count_sunday_the_firsts(start, end):
    """
    This function takes a start date and end date and finds
    all of the sundays that land on the first of the month
    within the allotted period.
    """
    day_to_check = start
    total_sundays = int()
    while day_to_check.weekday() != 6:
        day_to_check += ONE_DAY
    while day_to_check < end:
        day = day_to_check.day
        if day == 1:
            total_sundays += 1
            day_to_check += FOUR_WEEKS
        elif day <= 4:
            day_to_check += FOUR_WEEKS
        elif day <= 7:
            day_to_check += EIGHT_WEEKS
        elif day <= 11:
            day_to_check += THREE_WEEKS
        elif day <= 14:
            day_to_check += SEVEN_WEEKS
        elif day <= 18:
            day_to_check += TWO_WEEKS
        elif day <= 21:
            day_to_check += SIX_WEEKS
        elif day <= 25:
            day_to_check += ONE_WEEK
        elif day <= 28:
            day_to_check += FIVE_WEEKS
        else:
            day_to_check += NINE_WEEKS
    return total_sundays


def main():
    """
    Solves the problem.
    """
    start_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)
    return count_sunday_the_firsts(start_date, end_date)

if __name__ == "__main__":
    print main()
