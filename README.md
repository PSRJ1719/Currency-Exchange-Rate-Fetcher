# Currency Exchange Rate Fetcher

This Python script allows you to fetch real-time currency exchange rates and perform currency conversions. It uses the Free Currency Converter API to retrieve data and provides a simple command-line interface for users to interact with the script.

## Features

- **List Available Currencies:** Fetch and display a list of all available currencies and their symbols.
- **Convert Currencies:** Convert an amount from one currency to another using real-time exchange rates.
- **Get Exchange Rate:** Retrieve the current exchange rate between two specified currencies.
- **Error Handling:** Handles HTTP errors and invalid inputs gracefully.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Required Python packages: `requests`, `pprint`

You can install the required packages using pip:

pip install requests

## API Key

This script uses the Free Currency Converter API. You'll need an API key to use it. Replace the `API_KEY` variable in the script with your own API key.

API_KEY = "your_api_key_here"

## Usage

1. **Clone the Repository:**

   Clone this repository to your local machine using the following command:

   git clone https://github.com/PSRJ1719/Currency-Exchange-Rate-Fetcher.git

2. **Navigate to the Script Directory:**

   Navigate to the directory where the script is located:

   cd Currency-Exchange-Rate-Fetcher

3. **Run the Script:**

   You can run the script using the following command:

   python currency_converter.py

4. **Commands:**

   After running the script, you will be prompted to enter various commands to interact with the program:

   - `list`: Lists all available currencies along with their symbols.
   - `convert`: Converts a specified amount from one currency to another.
   - `rate`: Displays the exchange rate between two specified currencies.
   - `q`: Quits the program.

5. **Example Usage:**

   - **Listing Currencies:**
     Enter a command (q to quit): list

   - **Converting Currencies:**
     Enter a command (q to quit): convert
     Enter a base currency: USD
     Enter a currency to convert to: EUR
     Enter an amount in the base currency: 100

   - **Getting Exchange Rate:**
     Enter a command (q to quit): rate
     Enter a base currency: USD
     Enter a currency to convert to: JPY

## Error Handling

The script handles common errors such as invalid inputs, HTTP errors, and API response issues. Error messages are displayed in the console for easy debugging and user guidance.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue.
