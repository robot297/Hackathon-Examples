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
        """
        activity_response = requests.get(
                url=self.uat_url + f'customer/{customer_id}', 
                auth=self.basic_auth,
                headers=self.headers,
                json={
                    "customerID":customer_id
                },
                timeout=60
            )
        
        return activity_response