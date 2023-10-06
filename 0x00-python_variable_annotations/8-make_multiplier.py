#!/usr/bin/env python3

"""
Utilize type notations
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplies a float by the given multiplier.

    Take:
        multiplier (float): The value to multiply by.

    Returns:
        callable: A function that takes a float
        as input and returns the product.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a float by the multiplier.

        Parameters:
            x (float): The value to be multiplied.

        Returns:
            float: The product of x and the multiplier.
        """
        return x * multiplier

    return multiplier_function
