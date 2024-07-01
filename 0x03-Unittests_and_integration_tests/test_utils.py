#!/usr/bin/env python3
'''Parameterize a unit test'''
from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''unit test for access_nested_map function'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        A uIt tests the access_nested_map function by passing
        different nested maps and paths to check if the function
        correctly accesses the nested values and returns
        the expected output.

        Parameters:
        nested_map: dict - A dictionary representing the nested map.
        path: tuple - A tuple of keys representing
        the path to the value in the nested map.
        expected: any - The expected output value after accessing
        the nested map with the given path.
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)
