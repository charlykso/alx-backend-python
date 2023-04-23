#!/usr/bin/python3
"""
a TestAccessNestedMap class that inherits from unittest.TestCase
"""

import unittest
# from parameterized import parameterized, parameterized_class
from utils import access_nested_map as nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Implement the TestAccessNestedMap.test_access_nested_map
    method to test that the method returns what it is supposed to
    """
    # @parameterized.expand([])
    def test_access_nested_map(self):
        self.assertEqual(nested_map={"a": 1}, path=("a",))
        self.assertEqual(nested_map={"a": {"b": 2}}, path=("a",))
        self.assertEqual(nested_map={"a": {"b": 2}}, path=("a", "b"))


if __name__ == '__main__':
    unittest.main()
