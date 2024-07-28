#!/usr/bin/env python3
""" This module tests all functions in the file utils. """
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests functions in utils module"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Tests the access_nested_map func. """
        self.assertEqual(access_nested_map(nested_map, path), expected)
