"""Libraries for the core banking API.
"""
import requests
from .api_builder import APIBuilder

class CoreBanking(APIBuilder):
    """Helpers for interacting with the core banking API.
        Docs: 
    """
    def __init__(self, api_key, api_secret):
        """This creates the object for you to interact with the core banking API. 

        Args:
            api_key (string): The API key needed for authentication.
            api_secret (string): The API secret needed for authentication.
        """
        self.uat_url = 'https://alpha-api.usbank.com/innovation/bank-node/customer-accounts/v1/'
        super().__init__(api_key, api_secret)

    def find_customer(self, customer_id):
        """This method returns a single customer record associated with this Customer ID

        Args:
            customer_id (string): a unique customer id. 

        Returns: 
             Response: The response from the api including content and status code.
        """
        activity_response = requests.get(
                url=self.uat_url + f'customer/{customer_id}', 
                auth=self.basic_auth,
                headers=self.headers,
                timeout=60
            )
        return activity_response
    
    def find_accounts(self, customer_id): 
        """This method returns an array of accounts associated with this Customer ID

        Args:
            customer_id (string): a unique customer id
                    
        Returns: 
             Response: The response from the api including content and status code.
        """
        activity_response = requests.get(
                url=self.uat_url + f'customer/{customer_id}/accounts', 
                auth=self.basic_auth,
                headers=self.headers,
                timeout=60
            )
        return activity_response
    
    def account_details(self, account_id):
        """This method returns a single account record. (Provides the complete detailed listing for a single account.)

        Args:
            account_id (string): a unique account id
                    
        Returns: 
             Response: The response from the api including content and status code.
        """
        activity_response = requests.get(
                url=self.uat_url + f'account/{account_id}', 
                auth=self.basic_auth,
                headers=self.headers,
                timeout=60
            )
        return activity_response

    def list_cards(self, account_id):
        """This method returns a JSON array of card objects for a specific account

        Args:
            account_id (string): a unique account id
                    
        Returns: 
             Response: The response from the api including content and status code.
        """
        activity_response = requests.get(
                url=self.uat_url + f'account/{account_id}/cards', 
                auth=self.basic_auth,
                headers=self.headers,
                timeout=60
            )
        return activity_response
    
    def list_transactions(self, account_id, transaction_type, query_dates={}):
        """This method returns a JSON array of transactions for a specific account based on the input values. 
        It can be limited to certain transaction types and date ranges

        Args:
            account_id (string): a unique account id.
            transaction_type (string): type of transactions to retrieve. E.g., "FULL" "PUR" "MEMO" "PMT" "SHORT".
            query_dates (dict): (Optional) start and end dates for searching by transaction date range.

        Returns:
            _type_: _description_
        """
        activity_response = requests.get(
                url=self.uat_url + f'account/{account_id}/trans/{transaction_type}', 
                auth=self.basic_auth,
                headers=self.headers,
                params=query_dates,
                timeout=60
            )
        return activity_response