#!/usr/bin/env python3

"""
Utilize type notations
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Functions receives arguements of type list of mixed types
    Return: a float (sum)
    """

    return sum(mxd_lst)
