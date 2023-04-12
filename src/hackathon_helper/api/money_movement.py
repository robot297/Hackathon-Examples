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


    def deposit_money(self, account_id, amount, party, check_number=None):
        """This will deposit money to an account.

        Args:
            account_id (str): The contents of the request.
            amount (decimal): The amount to deposit in dollars.
            party (str): The payer name.
            check_number (str, optional): Defaults to none.
                The check number if applicable.

        Returns:
            Response: The response from the api including content and status code.
        """
        payload = {
            "accountID": account_id,
            "amount": float(amount),
            "checkNumber": check_number,
            "party": party
        }
        activity_response = requests.post(url=self.uat_url + 'activity/deposit',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def withdraw_money(self, account_id, amount, party, check_number=None):
        """This will withdraw money from an account.

        Args:
            account_id (str): The contents of the request.
            amount (decimal): The amount to deposit in dollars.
            party (str): The payer name.
            check_number (str, optional): Defaults to none.
                The check number if applicable.

        Returns:
            Response: The response from the api including content and status code.
        """
        payload = {
            "accountID": account_id,
            "amount": float(amount),
            "checkNumber": check_number,
            "party": party
        }
        activity_response = requests.post(url=self.uat_url + 'activity/deposit',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def card_purchase(self, card_number, first_name, last_name, expire_month, expire_year,
                      zipcode, cvv_code, amount, merchant, merchant_code, in_person = True):
        """This method attempts to create a card purchase and returns a valid receipt.

        Args:
            card_number (str): a valid credit card number.
            first_name (str): cardholder's first name.
            last_name (str): cardholder's last name.
            expire_month (str): expiration month (MM).
            expire_year (str): expiration year (YYYY).
            zipcode (str): Postal code associated with this card.
            amount (decimal): Purchase amount in dollars.
            merchant_code (str): The corresponding merchant code.
            cvv_code (str): Security code.
            in_person (bool, optional): Default true. 
                Indicates if purchase was made in-person (true) or online (false)

        Returns:
            Response: The response from the api including content and status code.
        """

        payload = {
            "cardNumber": card_number,
            "firstName": first_name,
            "lastName": last_name,
            "expMonth": expire_month,
            "expYear": expire_year,
            "zip": zipcode,
            "cvv": cvv_code,
            "amount": float(amount),
            "merchant": merchant,
            "mcc": merchant_code,
            "inPerson": in_person
        }

        activity_response = requests.post(url=self.uat_url + 'activity/card-purchase',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def card_purchase_reversal(self, account_id, transaction_id, reason):
        """This method attempts to reverse an existing card purchase and credits the account.

        Args:
            account_id (str): The contents of the request.
            transaction_id (str): the tranaction ID to be reversed.
            reason (str): Explanation for card reversal.
                Enum: "BILLING" "DISPUTE" "UNAUTHORIZED"

        Returns:
            Response: The response from the api including content and status code.
        """
        payload = {
            "accountID": account_id,
            "transactionID": transaction_id,
            "reason": reason
        }

        activity_response = requests.post(url=self.uat_url + 'activity/card-reverse',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def pay_card(self, account_id, amount, check_number=None):
        """This method attempts to pay a credit account according business rules.

        Args:
            account_id (str): The account id.
            amount (decimal): The amount to deposit in dollars.
            check_number (str, optional): Defaults to none.
                The check number if applicable.
        
        Returns:
            Response: The response from the api including content and status code.
        """
        payload = {
            "accountID": account_id,
            "amount": float(amount),
            "checkNumber": check_number
        }

        activity_response = requests.post(url=self.uat_url + 'activity/payment',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def card_purchase_from_digital_wallet(self, encrypted_card_data, wallet_id, amount,
                                          merchant, merchant_code):
        """This method attempts to create a card purchase through a digital wallet.
        A separate method can create the encrypted card data stream which is required for
        the digital wallet.

        Args:
            encrypted_card_data (str): the encrypted card data.
            wallet_id (str): the digital wallet identifier.
            ammount (decimal): Purchase amount.
            merchant (str): The merchant name.
            merchant_code (str): The corresponding merchant code
        
        Returns:
            Response: The response from the api including content and status code.
        """
        payload = {
            "encryptedCardData": encrypted_card_data,
            "walletID": wallet_id,
            "merchant": merchant,
            "mcc": merchant_code,
            "amount": amount
        }

        activity_response = requests.post(url=self.uat_url + 'activity/digital-wallet',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def external_funds_transfer(self, customer_id, account_id, routing_number,
                                external_account_id, amount):
        """This method moves funds from a specific customer account to a different
        customer account. Only savings or checking accounts are allowed.

        Args:
            customer_id (str): Customer identifier for the owner of the account.
            account_id (str): Unique identifier for the account sending funds.
            routing_number (str): Routing number for external account.
            external_account_id (str): Unique identifier for the external account receiving funds.
            amount (decimal): Transfer amount.
        
        Returns:
            Response: The response from the api including content and status code.
        """
        payload = {
            "customerID": customer_id,
            "accountID": account_id,
            "routingNumber": routing_number,
            "externalAccountID": external_account_id,
            "amount": float(amount)
        }
        activity_response = requests.post(url=self.uat_url + 'activity/external-transfer',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def internal_funds_transfer(self, customer_id, to_account_id, from_account_id, amount):
        """This method moves funds between two different accounts
        for the same customer according business rules.

        Args:
            customer_id (str): Customer identifier for the owner of the account.
            to_account_id (str): Unique identifier for the account receiving funds.
            from_account_id (str): Unique identifier for the account sending funds.
            amount (decimal): Transfer amount.
        
        Returns:
            Response: The response from the api including content and status code.
        """
        payload = {
            "customerID": customer_id,
            "toAccountID": to_account_id,
            "fromAccountID": from_account_id,
            "amount": amount
        }

        activity_response = requests.post(url=self.uat_url + 'activity/funds-transfer',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response

    def create_memo(self, account_id, memo):
        """This method notates a specific account with a custom message

        Args:
            account_id (str): The account id.
            memo (str): Memo string. (<= 256 characters)
        
        Returns:
            Response: The response from the api including content and status code.
        """
        payload = {
            "accountID": account_id,
            "memo": memo
        }
        activity_response = requests.post(url=self.uat_url + 'activity/memo',
                                          auth=self.basic_auth,
                                          headers=self.headers,
                                          json=payload,
                                          timeout=60)
        return activity_response
