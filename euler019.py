#!/usr/bin/env python
"""
This module solves Project Euler #1
"""

from datetime import date, timedelta

ONE_DAY = timedelta(days=1)
ONE_WEEK = timedelta(days=7)

def count_sunday_the_firsts(start, end):
    date = start
    total_sundays = int()
    while date.weekday() != 6:
        date += ONE_DAY
    while date < end:
        if date.day == 1:
            total_sundays += 1
        date += ONE_WEEK
    return total_sundays

def main():
    start_date = date(1901, 1, 1)
    end_date = date(2000, 12, 31)
    return count_sunday_the_firsts(start_date, end_date)

if __name__ == "__main__":
    print main()
