#!/usr/bin/env python
"""
This module solves Project Euler #19
"""

from datetime import date, timedelta

ONE_DAY = timedelta(days=1)
ONE_WEEK = timedelta(days=7)


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
        if day_to_check.day == 1:
            total_sundays += 1
        day_to_check += ONE_WEEK
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
