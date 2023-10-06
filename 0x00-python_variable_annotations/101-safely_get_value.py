#!/usr/bin/env python3

"""
Utilize type notations
"""

from typing import TypeVar, Mapping, Any, Union, Optional

K = TypeVar('K')
V = TypeVar('V', covariant=True)

def safely_get_value(dct: Mapping[K, V], key: K, default: Optional[V] = None) -> Union[V, None]:
    """
    Safely retrieves a value from a dictionary.

    Parameters:
        dct (Mapping[K, V]): The input dictionary.
        key (K): The key to retrieve.
        default (Optional[V], optional):
        The default value to return if the key is not found. 
        Defaults to None.

    Returns:
        Union[V, None]: The value associated with the key,
        or the default value if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
