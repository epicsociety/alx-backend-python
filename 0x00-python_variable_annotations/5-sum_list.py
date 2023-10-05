#!/usr/bin/env python3

"""
Utilize type notations
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Functions receives arguements of type list of floats
    Return: a float (sum)
    """

    return sum(input_list)
