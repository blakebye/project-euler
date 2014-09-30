#!/usr/bin/env python
"""
This module solves Project Euler #19
"""


def triangle_text_to_list(triangle_file):
    triangle_file = open(triangle_file)
    triangle = list()
    for line in triangle_file:
        triangle.append([int(x) for x  in line.split()])
    triangle_file.close()
    return triangle

def funnel(triangle):
    triangle.reverse()
    for line_index, line in enumerate(triangle):
        for index, element in enumerate(line):
            try:
                triangle[line_index +1][index] += max(element, line[index + 1])
            except IndexError:
                pass
    return triangle.pop().pop()

def main():
    """
    Solves the problem.
    """
    test_value = "p067_triangle.txt"
    return funnel(triangle_text_to_list(test_value))

if __name__ == "__main__":
    print main()
