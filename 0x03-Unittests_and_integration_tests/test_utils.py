#!/usr/bin/env python3
"""Parameterize a unit test"""
from utils import (
    access_nested_map,
    get_json,
    memoize,
)
from unittest.mock import patch, Mock
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
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(err.exception))


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.reset_mock()


class TestMemoize(unittest.TestCase):
    '''test memoize'''
    def test_memoize(self):
        '''Test memoize method to ensure that when a_property method
         called twice is correctly tested by calling a_method once'''
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            instance = TestClass()
            result1 = instance.a_property
            result2 = instance.a_property
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock.assert_called_once()
