#!/usr/bin/env python3

""" Testing for utils.access_nested_map
"""

import unittest
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """ Tests a class for utils.access_nested_map
    """

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test acesss_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",), KeyError),
                           ({"a": 1}, ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test acesss_nested_map exception
        """
        self.assertRaises(expected)


class TestGetJson(unittest.TestCase):
    """ Test class for utils.get_json
    """

    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    def test_get_json(self, test_url, test_payload):
        """ Test get_json and create mock test
        """
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            get_json_response = get_json(test_url)
            self.assertEqual(get_json_response, test_payload)
            mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Test class for utils.memoize
    """

    def test_memoize(self):
        """ Test util.memoize
        """
        class TestClass:
            """ A example class to test against
            """

            def a_method(self):
                """ returns 42
                """
                return 42

            @memoize
            def a_property(self):
                """ Memoizis a_method and returns 42
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test_class = TestClass()
            a_property_return = test_class.a_property
            a_property_return = test_class.a_property
            self.assertEqual(a_property_return, 42)
            mock.assert_called_once()
