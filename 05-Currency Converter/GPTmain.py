import requests

def get_currency_input(prompt):
    return input(prompt).upper()

def get_amount_input():
    while True:
        try:
            amount = float(input("Enter amount to convert: "))
            if amount <= 0:
                print("The amount must be greater than 0. Please try again.")
            else:
                return amount
        except ValueError:
            print("The amount must be a valid number. Please try again.")

def convert_currency(api_key, init_currency, target_currency, amount):
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"
    headers = {
        "apikey": api_key
    }
    response = requests.get(url, headers=headers)
    return response

def main():
    api_key = "Tpnb1VT67Il5TvJdwjZQBohb8enlfHH2"  # Replace with a secure method to handle the API key
    print("Welcome to the Currency Converter!")
    
    init_currency = get_currency_input("Enter the initial currency (e.g., USD, EUR): ")
    target_currency = get_currency_input("Enter the target currency (e.g., GBP, JPY): ")
    amount = get_amount_input()

    print(f"\nConverting {amount} {init_currency} to {target_currency}...\n")
    
    response = convert_currency(api_key, init_currency, target_currency, amount)

    if response.status_code != 200:
        print(f"Status code: {response.status_code}\nThere was a problem with the request. Please try again later.")
    else:
        result = response.json()
        if result.get("success"):
            converted_amount = result.get("result")
            print(f"Conversion Successful!")
            print(f"{amount} {init_currency} is approximately {converted_amount:.2f} {target_currency}.")
            print(f"Exchange Rate: 1 {init_currency} = {converted_amount/amount:.4f} {target_currency}")
        else:
            print(f"Error: {result.get('error', {}).get('info')}")

if __name__ == "__main__":
    main()
