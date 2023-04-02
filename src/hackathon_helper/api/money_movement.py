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


    def deposit_money(self, payload):
        """This will deposit money to an account.

        Args:
            payload (dict): The contents of the request.

        Returns:
            Response: The response from the api including content and status code.
        """
        activity_response = requests.post(url=self.uat_url + 'activity/deposit',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def withdraw_money(self, payload):
        """This will withdraw money from an account.

        Args:
            payload (dict): The contents of the request.

        Returns:
            Response: The response from the api including content and status code.
        """
        activity_response = requests.post(url=self.uat_url + 'activity/deposit',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response
