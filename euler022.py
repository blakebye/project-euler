#!/usr/bin/env python
"""
This module solves Project Euler #22
"""

def file_to_sorted_list(filename):
    """
    This function takes a filename of a file with names listed
    in it, and returns all of those names in an alphabetic list.
    """
    f = open(filename)
    line = f.readline()
    names = line.split(",")
    names = [name.strip('"') for name in names]
    names.sort()
    return names

def word_score(word):
    """
    This function takes a word and tells how many "points" it
    has, with a = 1, z = 26 and the word is the sum.
    """
    points = int()
    for char in word:
        points += ord(char) - 64
    return points

def names_scores(filename):
    """
    This function takes a filename of a file with names listed
    in it, and returns the word score of each name listed in it
    multiplied by the line on which that name is, summed.
    """
    names = file_to_sorted_list(filename)
    total = int()
    for index, name in enumerate(names, 1):
        total += word_score(name) * index
    return total


def main():
    test_value = "p022_names.txt"
    return names_scores(test_value)

if __name__ == "__main__":
    print main()
