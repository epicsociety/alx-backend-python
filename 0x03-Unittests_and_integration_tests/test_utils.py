#!/usr/bin/env python3
"""
Module contain tests cases set up with parameterized.expand
"""


import unittest
from unittest.mock import Mock, patch
from typing import (
    Mapping,
    Sequence,
    Any,
)
from parameterized import parameterized
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json
memoize = __import__("utils").memoize



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
        """ Testing with assertRaises"""
        with self.assertRaises(KeyError):
            access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Checks whether utils.get_json return expected output
        """

    def test_get_json(self):
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        for url, payload in test_cases:
            with patch("requests.get") as mock_get:
                # Create a Mock object to simulate the response
                mock_response = Mock()
                mock_response.json.return_value = payload
                mock_get.return_value = mock_response

                result = get_json(url)

                self.assertEqual(result, payload)
                mock_get.assert_called_once_with(url)

class TestMemoize(unittest.TestCase):
    """ class has a test_memoize method"""

    def test_memoize(self):
        """ Sets up mock tests"""

        class TestClass:
            """ A simple class """

            def a_method(self):
                """ A simple method """
                return 42

            @memoize
            def a_property(self):
                """ memoizing method """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()
