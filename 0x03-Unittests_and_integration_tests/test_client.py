#!/usr/bin/env python3

""" Testing the client
"""

import unittest
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock
from utils import get_json
from client import GithubOrgClient
import client
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Tests class for GithubOrgClient
    """

    @parameterized.expand(
        [("google", {"google", True}), ("abc", {"abc", True})])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """ Tests the GithubOrgClient.org method
        """
        get_patch.return_value = expected
        gh_client = GithubOrgClient(org)
        self.assertEqual(gh_client.org, expected)
        get_patch.assert_called_once_with(f'https://api.github.com/orgs/{org}')

    def test_public_repos_url(self):
        """ Test the GithubOrgClient._public_repos_url
        """
        expected = "www.geoff.com"
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value={'repos_url': expected})):
            gh_client = GithubOrgClient("adobe")
            self.assertEqual(gh_client._public_repos_url, expected)

    """ @patch('client.get_json')
    def test_public_repos(self, get_patch):

        repo1={"license1": {"key": "my_license"}},
        repo2={"license2": {"key": "other_license"}}

        get_patch.return_value = [repo1, repo2]

        with patch('client.GithubOrgClient._public_repos_url',
        PropertyMock(return_value={'www.geoff.com'})) as mock:
            gh_client = GithubOrgClient('adobe')
            self.assertEqual(gh_client.public_repos(), ['repo1', 'repo2'])
            self.assertEqual(gh_client.public_repos('a'), ['geoff'])
            get_json.assert_called_once_with('www.geoff.com')
            mock.assert_called_once_with() """

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, repo, license_key, expected):
        """ Test GithubOrgClient.has_license method
        """
        self.assertEqual(
            GithubOrgClient.has_license(
                repo, license_key), expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Test class for GithubOrgClient.public_repos
    """

    @classmethod
    def setUpClass(cls):
        """ Setup tests for class GithubOrgClient
        """
        pass

    def tearDownClass(self):
        """ Teardown tests for GithubOrgClient
        """
        pass

    def test_public_repos_with_license(self):
        """ Test GithubOrgClient.public_repos method
        """
        pass

    def test_public_repos(self):
        """ Test GithubOrgClient.public_repos method
        """
        pass

    def test_public_repos_with_license(self):
        """ Test public_repos
        """
        pass
