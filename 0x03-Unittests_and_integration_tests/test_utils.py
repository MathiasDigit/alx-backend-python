#!/usr/bin/env python3
"""A test module to test functions from the utils module."""

from parameterized import parameterized
import unittest
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access_nested_map raises KeyError on bad path."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """Test class for get_json using mocked requests."""

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, url, expected):
        """Test get_json returns expected dictionary from URL."""
        with patch('utils.requests.get') as mock_get:
            def mock_behaviour(url):
                response = Mock()
                if url == 'http://example.com':
                    response.json.return_value = {"payload": True}
                    return response
                if url == 'http://holberton.io':
                    response.json.return_value = {"payload": False}
                    return response
                response.json.return_value = ValueError('error no value')
                return response

            mock_get.side_effect = mock_behaviour
            output = get_json(url)
            self.assertEqual(output, expected)
            mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches method results after first call."""

        class TestClass:
            def a_method(self):
                """Returns a constant value."""
                return 42

            @memoize
            def a_property(self):
                """Calls a_method (but should only do it once)."""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42
                          ) as mock_method:
            obj = TestClass()
            result1 = obj.a_property
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
