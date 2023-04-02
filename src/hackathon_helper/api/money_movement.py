"""Libraries for the money movement API.
"""
import requests
from .api_builder import APIBuilder

class MoneyMovement(APIBuilder):
    """Functions for the money movement API.
    """

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
