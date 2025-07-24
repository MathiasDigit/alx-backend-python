#!/usr/bin/env python3
"""Test module for the GithubOrgClient class."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""

        # Set the mock return value of get_json to simulate API response
        expected_payload = {"login": org_name, "id": 123}

        # Configure the mock to return the expected payload
        mock_get_json.return_value = expected_payload

        # Create an instance of GithubOrgClient with the provided org name
        client = GithubOrgClient(org_name)

        # Call the org method which should internally call get_json
        result = client.org

        # Assert that the returned result matches the mocked payload
        self.assertEqual(result, expected_payload)

        # Assert that get_json was called exactly once with the expected URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
