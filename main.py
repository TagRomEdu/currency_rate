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


def main():
    while True:
        currency = input("Введите название валюты (USD или EUR): ").upper()
        if currency not in ("USD", "EUR"):
            print("Некорректный ввод")
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Курс {currency} к рублю: {rate:.2f}")

        data = {"rate": rate, "timestamp": timestamp}
        save_to_json(data)

        choice = input("Выберите действие: (1 - продолжить, 2 - выйти)\n")
        if choice == 1:
            continue
        elif choice == 2:
            break
        else:
            print("Incorrect input")


if __name__ == "__main__":
    main()
