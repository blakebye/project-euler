#!/usr/bin/env python
"""
This module solves Project Euler #18
"""


def generate_triangle_number(which):
    """
    This function will return a triangle number. Which
    one will be determined by the input.
    """
    return int(which / 2. * (which + 1))


def triangle_text_to_lists(triangle):
    """
    This function takes a triangle string and gives back
    a triangle-type list, which is just a list of lists.
    """
    triangle_lists = list()
    line = list()
    values = triangle.split()
    stepper = 1
    tri_number = generate_triangle_number(stepper)
    for index, value in enumerate(values):
        if index != tri_number:
            line.append(int(value))
        else:
            stepper += 1
            tri_number = generate_triangle_number(stepper)
            triangle_lists.append(line)
            line = [int(value)]
    triangle_lists.append(line)
    return triangle_lists


def funnel(triangle):
    """
    This function takes a triangle-type list and turns it upside down.
    Then a parent's largest child "drips" into them, all the way down.
    The result is the bottom of the triangle having the highest value
    of the sum of path from top to bottom.
    """
    triangle.reverse()
    for line_index, line in enumerate(triangle):
        for index, element in enumerate(line):
            try:
                triangle[line_index + 1][index] += max(element,
                                                       line[index + 1])
            except IndexError:
                pass
    return triangle.pop().pop()


def main():
    """
    Solves the problem.
    """
    test_value = "75 " \
                 "95 64 " \
                 "17 47 82 " \
                 "18 35 87 10 " \
                 "20 04 82 47 65 " \
                 "19 01 23 75 03 34 " \
                 "88 02 77 73 07 63 67 " \
                 "99 65 04 28 06 16 70 92 " \
                 "41 41 26 56 83 40 80 70 33 " \
                 "41 48 72 33 47 32 37 16 94 29 " \
                 "53 71 44 65 25 43 91 52 97 51 14 " \
                 "70 11 33 28 77 73 17 78 39 68 17 57 " \
                 "91 71 52 38 17 14 91 43 58 50 27 29 48 " \
                 "63 66 04 68 89 53 67 30 73 16 69 87 40 31 " \
                 "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
    return funnel(triangle_text_to_lists(test_value))

if __name__ == "__main__":
    print main()
