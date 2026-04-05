"""
Unit tests for the WebService class using unittest and mock.
"""
import unittest
from unittest.mock import MagicMock, patch
import requests
from .web_service import WebService


class TestWebService(unittest.TestCase):
    """
    Test suite for validating WebService data retrieval and error handling.
    """

    def setUp(self) -> None:
        """
        Set up a WebService instance and a default URL before each test.
        """
        self.web_service = WebService()
        self.url = "https://www.google.com"

    @patch('requests.get')
    def test_get_data_success(self, mock_get: MagicMock) -> None:
        """
        Test successful data retrieval from the web service.
        """
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test" }

        mock_get.return_value = mock_response

        result = self.web_service.get_data(self.url)

        self.assertEqual(result, {'data': 'test'})
        mock_get.assert_called_with(self.url)

    @patch('requests.get')
    def test_get_data_404_error(self, mock_get: MagicMock) -> None:
        """
        Test the service behavior when a 404 Not Found error occurs.
        """
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")

        mock_get.return_value = mock_response

        result = self.web_service.get_data(self.url)

        self.assertIn("error", result)
        self.assertIn("404 Not Found", result["error"])

    @patch('requests.get')
    def test_get_data_connection_error(self, mock_get: MagicMock) -> None:
        """
        Test the service behavior when a network connection error occurs.
        """
        mock_get.side_effect = requests.exceptions.ConnectionError("connection error")

        result = self.web_service.get_data(self.url)

        self.assertIn("error", result)
        self.assertIn("Other error occurred", result["error"])


if __name__ == '__main__':

    unittest.main()
