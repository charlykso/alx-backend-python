#!/usr/bin/python3
"""
a TestAccessNestedMap class that inherits from unittest.TestCase
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Implement the TestAccessNestedMap.test_access_nested_map
    method to test that the method returns what it is supposed to
    """
    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2],
    ])
    def test_access_nested_map(self,  nested_map, path, expected_output):
        self.assertEqual(access_nested_map(nested_map, path), expected_output)


    @parameterized.expand([
        [{}, ("a",), "Key 'a' not found in nested map"],
        [{"a": 1}, ("a", "b"), "Key 'b' not found in nested map"],
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_error):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), expected_error)


if __name__ == '__main__':
    unittest.main()
