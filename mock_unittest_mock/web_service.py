"""
Module for interacting with external web services using the requests library.
"""
# pylint: disable=too-few-public-methods
import requests


class WebService:
    """
    A service class to handle HTTP GET requests and process JSON data.
    """

    def get_data(self, url: str) -> dict:
        """
        Fetch JSON data from a given URL and handle potential errors.
        Args:
        url (str): The target URL to fetch data from.
        Returns:
        Dict[str, Any]: A dictionary containing the JSON response
                        or an error message.
        """
        try:
            response: requests.Response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as errh:
            return {"error": f" HTTP error occurred: {errh}"}
        except requests.exceptions.RequestException as err:
            return {"error": f"Network or Request error occurred: {err}"}
