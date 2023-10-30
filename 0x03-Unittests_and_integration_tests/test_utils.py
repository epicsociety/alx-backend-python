#!/usr/bin/env python3
"""
Module contain tests cases set up with parameterized.expand
"""


import unittest
from typing import (
    Mapping,
    Sequence,
    Any,
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
                               nested_map: Any) -> bool:
        """ The testing method """
        self.assertEqual(access_nested_map(map, path), nested_map)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, map: Mapping, path: Sequence):
        """ Testing with asssertRaises"""
        with self.assertRaises(KeyError):
            access_nested_map(map, path)
