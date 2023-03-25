import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from pprint import pprint


if __name__ == "__main__":

    load_dotenv()

    API_KEY = os.getenv('api_key')
    API_SECRET = os.getenv('api_secret')
    basic = HTTPBasicAuth(API_KEY, API_SECRET)

    uat_url = 'https://alpha-api.usbank.com/innovation/bank-node/money-movement/v1/'

    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        "accountID": "00000",
        "amount": 10,
        "checkNumber": "",
        "party": "Test"
    }
    
    activity_response = requests.post(url=uat_url + 'activity/deposit', auth=basic, headers=headers, json=payload).json()
    pprint(activity_response)
