#!/usr/bin/env python3

"""
Utilize type notations
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with elements from `lst` and their lengths.

    Parameters:
        lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
        where the first element is a sequence
        from `lst` and the second element is its length.
    """
    return [(i, len(i)) for i in lst]
