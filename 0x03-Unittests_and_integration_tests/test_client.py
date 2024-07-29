#!/usr/bin/env python3
""" This module tests all the methods in GithubOrgClient class."""
from unittest.mock import patch, Mock, PropertyMock
import unittest
from client import GithubOrgClient
from utils import get_json
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """ Tests the class methods in the class """
    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch('client.get_json')
    def test_org(self, rez, mock_get):
        """ Tests case for the org method """
        examp = GithubOrgClient(rez)
        examp.org()
        mock_get.assert_called_once_with(f'https://api.github.com/orgs/{rez}')

    def test_public_repos_url(self):
        """ Tests the case for public_repos_url method"""
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_prop:
            mock_prop.return_value = "hello"
            instan = GithubOrgClient("google")
            self.assertEqual(instan._public_repos_url, "hello")
            mock_prop.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test case for public_repos method."""
        payload = [{"name": "Adnan"}, {"name": "Obuya"}]
        mock_get_json.return_value = payload
        x = 'https://api.github.com/orgs/google/repos'
        y = 'https://api.github.com/orgs/google/repos'
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_pub_rep:
            mock_pub_rep.return_value = x
            instan = GithubOrgClient("google")
            rez = instan.public_repos()
            self.assertEqual(rez, ["Adnan", "Obuya"])
            mock_get_json.assert_called_once_with(y)
            mock_pub_rep.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, licensed_key, expected):
        """ Tests the has license method"""
        self.assertEqual(GithubOrgClient.has_license(repo, licensed_key),
                         expected)


@parameterized_class((
    'org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
        TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Intergration test on public repos method"""
    @classmethod
    def setUpClass(cls):
        """ Sets up class"""
        cls.get_patcher = patch('requests.get')
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ Exits the tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ tests the public repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.repos_payload, self.repos_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("XLICENSE"), [])
        self.mock.assert_called()
