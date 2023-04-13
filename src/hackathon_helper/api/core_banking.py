"""Libraries for the core banking API.
"""
import requests
from .api_builder import APIBuilder

class CoreBanking(APIBuilder):
    """Helpers for interacting with the core banking API.
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
        """This method returns a single customer record associated with this Customer ID.

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

    def list_accounts(self, customer_id):
        """This method returns an array of accounts associated with this Customer ID.

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
        """This method returns a single account record.
        (Provides the complete detailed listing for a single account.)

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
        """This method returns a JSON array of card objects for a specific account.

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

    def list_transactions(self, account_id, transaction_type, **kwargs):
        """This method returns a JSON array of transactions for a specific
        account based on the input values. It can be limited to certain transaction
        types and date ranges.

        Args:
            account_id (string): a unique account id.
            transaction_type (string): type of transactions to retrieve. 
                E.g., "FULL" "PUR" "MEMO" "PMT" "SHORT".
            start (string, optional): start date for searching by
                transaction date range. Must use format: "YYYY-MM-DD"
            end (string, optional): end date for searching by
                transaction date range. Must use format: "YYYY-MM-DD"
                
        Returns:
            Response: The response from the api including content and status code.
        """
        optional_params = kwargs.keys()

        if 'start' in optional_params and 'end' in optional_params:
            query_dates = {'start': kwargs['start'], 'end': kwargs['end']}
        else:
            query_dates = None

        activity_response = requests.get(
                url=self.uat_url + f'account/{account_id}/trans/{transaction_type}',
                auth=self.basic_auth,
                headers=self.headers,
                params=query_dates,
                timeout=60
            )
        return activity_response

    def create_credit_card(self, customer_id, nickname=None, account_type=None, credit_limit=None):
        """This method generates a new credit card account for a specific customer account.

        Args:
            customer_id (string): a unique customer id
            nickname (optional, string): Account nickname
            account_type (optional, string): type of mock account; enum[CCD, BCD]
            credit_limit (optional, float): Credit limit for new card account

        Returns:
            Response: The response from the api including content and status code.
        """


        payload = {
                "nickname": str(nickname),
                "accountType": str(account_type),
                "creditLimit": float(credit_limit)
        }

        activity_response = requests.post(
                url=self.uat_url + f'account/{customer_id}/credit',
                auth=self.basic_auth,
                headers=self.headers,
                json=payload,
                timeout=60
            )
        return activity_response

    def create_deposit_account(self, customer_id,  nickname=None,
                               account_type=None, open_balance=None):
        """This method generates a new deposit account for a specific customer account.

        Args:
            customer_id (string): a unique customer id
            nickname (optional, string): Account nickname
            account_type (optional, string): type of mock account; enum[CCD, BCD]
            open_balance (optional, float): Credit limit for new card account

        Returns:
            Response: The response from the api including content and status code.
        """
        payload = {
                "nickname": str(nickname),
                "accountType": str(account_type),
                "openBalance": float(open_balance)
        }
        activity_response = requests.post(
                url=self.uat_url + f'account/{customer_id}/dda',
                auth=self.basic_auth,
                headers=self.headers,
                json=payload,
                timeout=60
            )
        return activity_response

    def find_transaction(self, transaction_id):
        """This method returns a JSON object of a single transaction.

        Args:
            transaction_id (string): a unique transaction id

        Returns: 
            Response: The response from the api including content and status code.
        """
        activity_response = requests.get(
                url=self.uat_url + f'transaction/{transaction_id}',
                auth=self.basic_auth,
                headers=self.headers,
                timeout=60
            )
        return activity_response
