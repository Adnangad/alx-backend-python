#!/usr/bin/env python3
""" This module tests all the methods in GithubOrgClient class."""
from unittest.mock import patch, Mock, PropertyMock
import unittest
from client import GithubOrgClient
from utils import get_json
from parameterized import parameterized


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
        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=PropertyMock) as mock_prop:
            mock_prop.return_value = "hello"
            instan = GithubOrgClient("google")
            self.assertEqual(instan._public_repos_url, "hello")
            mock_prop.assert_called_once()