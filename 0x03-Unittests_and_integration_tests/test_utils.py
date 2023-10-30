#!/usr/bin/env python3
"""
Module contain tests cases set up with parameterized.expand
"""


import unittest
from typing import (
    Mapping,
    Sequence,
)
from parameterized import parameterized
access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """class set up to implement the test methods"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map: Mapping, path: Sequence,
                               nested_map: Mapping) -> bool:
        """ The testing method """
        produced_map = access_nested_map(map, path)
        self.assertEqual(self, produced_map, nested_map)
