#!/usr/bin/env python3
"""Test module for the GithubOrgClient class."""

import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized, parameterized_class
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


def test_public_repos_url(self):
    """Test that _public_repos_url returns the correct URL from org payload."""
    # Payload to be returned by the mocked 'org' property
    mock_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}

    # Patch the 'org' property using PropertyMock
    with patch.object(GithubOrgClient, 'org', return_value=mock_payload):
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, mock_payload["repos_url"])


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient."""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns expected list of repo names."""

        # Simulated JSON payload returned by get_json
        mocked_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        # Simulated URL that would normally come from _public_repos_url
        mocked_repos_url = "https://api.github.com/orgs/test-org/repos"

        # Set return value for the get_json mock
        mock_get_json.return_value = mocked_repos_payload

        # Patch the _public_repos_url property
        with patch.object(
               GithubOrgClient,
               "_public_repos_url",
               new=mocked_repos_url
        ):
            client = GithubOrgClient("test-org")
            result = client.public_repos()

            # Assert the result is the list of repo names
            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            # Ensure mocks were each called exactly once
            mock_get_json.assert_called_once_with(mocked_repos_url)


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient."""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license returns True only when license matches key."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


# Fixtures
REPOS_FIXTURE = [
    {
        "name": "episodes.dart",
        "license": {"key": "bsd-3-clause"}
    },
    {
        "name": "cpp-netlib",
        "license": {"key": "apache-2.0"}
    }
]


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient"""

    @patch(
            'client.GithubOrgClient._public_repos_json',
            return_value=REPOS_FIXTURE
             )
    def test_public_repos(self, mock_repos):
        """Test public_repos returns all repo names"""
        client = GithubOrgClient("google")
        expected = ["episodes.dart", "cpp-netlib"]
        self.assertEqual(client.public_repos(), expected)

    @patch(
            'client.GithubOrgClient._public_repos_json',
            return_value=REPOS_FIXTURE
            )
    def test_public_repos_with_license(self, mock_repos):
        """Test public_repos filters by license='apache-2.0'"""
        client = GithubOrgClient("google")
        expected = ["cpp-netlib"]
        self.assertEqual(client.public_repos(license="apache-2.0"), expected)


if __name__ == '__main__':
    unittest.main()
