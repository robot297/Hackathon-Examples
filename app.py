import os
from dotenv import load_dotenv
from api.money_movement import MoneyMovement


if __name__ == "__main__":

    load_dotenv()

    API_KEY = os.getenv('api_key')
    API_SECRET = os.getenv('api_secret')

    payload = {
        "accountID": "00000",
        "amount": 10,
        "checkNumber": "",
        "party": "Test"
    }
    
    money_movement = MoneyMovement(API_KEY, API_SECRET)

    response = money_movement.post_money(payload)

    print(response.json())
