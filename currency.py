import requests

API_KEY = 'fca_live_QiRD4yaE7K1aJQIAfVLojfu8J2KPxSXPYkDxxTzc'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"
CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "RMB"]

def get_exchange_rates(base_currency):
    """Fetch exchange rates for a given base currency."""
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base_currency}&currencies={currencies}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        data = response.json()
        return data["data"]
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_exchange_rates(base_currency, rates):
    """Display exchange rates, excluding the base currency."""
    if base_currency in rates:
        del rates[base_currency]
    for currency, rate in rates.items():
        print(f"{currency}: {rate}")

def main():
    while True:
        base_currency = input("Enter the base currency (q to quit): ").upper()
        if base_currency == "Q":
            break
        exchange_rates = get_exchange_rates(base_currency)
        if exchange_rates:
            display_exchange_rates(base_currency, exchange_rates)

if __name__ == "__main__":
    main()
