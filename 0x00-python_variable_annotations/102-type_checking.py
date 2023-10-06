#!/usr/bin/env python3

"""
Utilize type notations
"""


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Changed to a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Changed to an integer
