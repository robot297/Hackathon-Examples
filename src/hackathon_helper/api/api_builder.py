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
        self.uat_url = 'https://alpha-api.usbank.com/innovation/bank-node/money-movement/v1/'
        self.headers = { 'Content-Type': 'application/json' }
        self.basic_auth = HTTPBasicAuth(api_key, api_secret)
