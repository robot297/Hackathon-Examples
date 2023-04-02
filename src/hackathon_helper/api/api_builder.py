"""Parent class for building out the APIs
"""
from requests.auth import HTTPBasicAuth

class APIBuilder:
    """Parent class for building out the APIs
    """

    def __init__(self, api_key, api_secret):
        """This creates the object for you to interacting with money movement API.

        Args:
            API_KEY (string): The API key needed for authentication.
            API_SECRET (string): The API secret needed for authentication.
        """
        self.headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        self.basic_auth = HTTPBasicAuth(api_key, api_secret)
