"""Libraries for the money movement API.
"""
from requests.auth import HTTPBasicAuth
import requests

class MoneyMovement:
    """Functions for the money movement API.
    """

    def __init__(self, API_KEY, API_SECRET):
        """This creates the object for you to interacting with money movement API.

        Args:
            API_KEY (string): The API key needed for authentication.
            API_SECRET (string): The API secret needed for authentication.
        """
        self.uat_url = 'https://alpha-api.usbank.com/innovation/bank-node/money-movement/v1/'
        self.headers = { 'Content-Type': 'application/json' }
        self.basic_auth = HTTPBasicAuth(API_KEY, API_SECRET)


    def post_money(self, payload):
        """This will post money to an account.

        Args:
            payload (dict): The contents of the request.

        Returns:
            Response: The reponse from the api including content and status code.
        """
        activity_response = requests.post(url=self.uat_url + 'activity/deposit',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload)
        return activity_response
