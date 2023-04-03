"""Libraries for the money movement API.
"""
import requests
from .api_builder import APIBuilder

class MoneyMovement(APIBuilder):
    """Functions for the money movement API.
    """

    def __init__(self, api_key, api_secret):
        """This creates the object for you to interact with money movement API.

        Args:
            api_key (string): The API key needed for authentication.
            API_SECRET (string): The API secret needed for authentication.
        """
        self.uat_url = 'https://alpha-api.usbank.com/innovation/bank-node/money-movement/v1/'
        super().__init__(api_key, api_secret)


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

    def card_purchase(self, payload):
        """This method attempts to create a card purchase and returns a valid receipt.

        Args:
            payload (dict): The contents of the request.

        Returns:
            Response: The response from the api including content and status code.
        """
        activity_response = requests.post(url=self.uat_url + 'activity/card-purchase',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def card_purchase_reversal(self, payload):
        """This method attempts to reverse an existing card purchase and credits the account.

        Args:
            payload (dict): The contents of the request.
        
        Returns:
            Response: The response from the api including content and status code.
        """
        activity_response = requests.post(url=self.uat_url + 'activity/card-reverse',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def pay_card(self, payload):
        """This method attempts to pay a credit account according business rules.

        Args:
            payload (dict): The contents of the request.
        
        Returns:
            Response: The response from the api including content and status code.
        """
        activity_response = requests.post(url=self.uat_url + 'activity/payment',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def card_purchase_from_digital_wallet(self, payload):
        """This method attempts to create a card purchase through a digital wallet.
        A separate method can create the encrypted card data stream which is required for
        the digital wallet.

        Args:
            payload (dict): The contents of the request.
        
        Returns:
            Response: The response from the api including content and status code.
        """
        activity_response = requests.post(url=self.uat_url + 'activity/digital-wallet',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def external_funds_transfer(self, payload):
        """This method moves funds from a specific customer account to a different
        customer account. Only savings or checking accounts are allowed.

        Args:
            payload (dict): The contents of the request.
        
        Returns:
            Response: The response from the api including content and status code.
        """
        activity_response = requests.post(url=self.uat_url + 'activity/external-transfer',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def internal_funds_transfer(self, payload):
        """This method moves funds between two different accounts
        for the same customer according business rules.

        Args:
            payload (dict): The contents of the request.
        
        Returns:
            Response: The response from the api including content and status code.
        """
        activity_response = requests.post(url=self.uat_url + 'activity/funds-transfer',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def create_memo(self, payload):
        """This method notates a specific account with a custom message

        Args:
            payload (dict): The contents of the request.
        
        Returns:
            Response: The response from the api including content and status code.
        """
        activity_response = requests.post(url=self.uat_url + 'activity/memo',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response
