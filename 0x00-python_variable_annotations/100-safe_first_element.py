#!/usr/bin/env python3

"""
Utilize type notations
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    Returns the first element of a sequence,
    or None if the sequence is empty.

    Parameters:
        lst (Sequence): Any iterable sequence.

    Returns:
        Union[Any, None]: The first element of the sequence,
        or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
