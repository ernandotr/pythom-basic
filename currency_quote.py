import requests

def get_currency_quote(base_currency, target_currency):
    """
    Fetches the current exchange rate for a given base currency to a target currency.

    :param base_currency: The currency code to convert from (e.g., 'USD').
    :param target_currency: The currency code to convert to (e.g., 'BRL').
    :return: The exchange rate as a float, or None if the request fails.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates'].get(target_currency)
    except requests.RequestException as e:
        print(f"Error fetching exchange rate: {e}")
        return None 

# Example usage:
if __name__ == "__main__":
    base = "USD"
    target = "BRL"
    rate = get_currency_quote(base, target)
    if rate is not None:
        print(f"Exchange rate from {base} to {target}: {rate}")
    else:
        print("Failed to retrieve exchange rate.")

    base = "EUR"
    target = "BRL"
    rate = get_currency_quote(base, target)
    if rate is not None:
        print(f"Exchange rate from {base} to {target}: {rate}")
    else:
        print("Failed to retrieve exchange rate.")