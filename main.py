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

