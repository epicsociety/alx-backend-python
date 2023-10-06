#!/usr/bin/env python3

"""
Utilize type notations
"""

from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Utilize type notations

    Parameters:
        k (str): The input string.
        v (Union[int, float]): The input value, either an int or a float.

    Returns:
        Tuple[str, float]: with string `k` and the square of `v`.
    """

    return k, v**2
