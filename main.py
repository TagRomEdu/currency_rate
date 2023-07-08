import os
import json
import requests
from datetime import datetime


API_KEY = os.getenv('API_KEY')
CURRENCY_RATES_FILE = "currency_rates.json"

def get_currency_rate(currency: str) -> float:
    """
    Получает курс валюты от API и возвращает его в виде float\
    """
    url = "https://api.apilayer.com/exchangerates_data/latest"
    params = {"apikey": API_KEY, "base": currency}

    response = requests.get(url, params)

    return response.json()['rates']['RUB']


def save_to_json(data: dict) -> None:
    """
    Сохраняет данные в JSON-файл
    """
    with open(CURRENCY_RATES_FILE, 'a') as file:
        if os.stat(CURRENCY_RATES_FILE).st_size == 0:
            json.dump([data], file)
        else:
            with open(CURRENCY_RATES_FILE) as j_file:
                data_lst = json.load(j_file)
            data_lst.append(data)
            with open(CURRENCY_RATES_FILE, 'w') as new_file:
                json.dump([data], new_file)
