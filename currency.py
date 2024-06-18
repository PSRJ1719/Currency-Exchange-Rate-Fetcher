from requests import get, HTTPError
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    try:
        response = get(url)
        response.raise_for_status()
        data = response.json().get('results', {})
        sorted_data = sorted(data.items())
        return sorted_data
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return []


def print_currencies(currencies):
    for name, currency in currencies:
        currency_name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {currency_name} - {symbol}")


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    try:
        response = get(url)
        response.raise_for_status()
        data = response.json()
        if not data:
            print('Invalid currencies.')
            return None
        rate = list(data.values())[0]
        print(f"{currency1} -> {currency2} = {rate}")
        return rate
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    return None


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


def main():
    currencies = get_currencies()
    if not currencies:
        print("Failed to retrieve currencies. Exiting...")
        return

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    commands = {
        "list": lambda: print_currencies(currencies),
        "convert": lambda: convert(
            input("Enter a base currency: ").upper(),
            input("Enter a currency to convert to: ").upper(),
            input("Enter an amount in the base currency: ")
        ),
        "rate": lambda: exchange_rate(
            input("Enter a base currency: ").upper(),
            input("Enter a currency to convert to: ").upper()
        ),
    }

    while True:
        command = input("Enter a command (q to quit): ").lower()
        if command == "q":
            break
        elif command in commands:
            commands[command]()
        else:
            print("Unrecognized command!")


if __name__ == "__main__":
    main()
