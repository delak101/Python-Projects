import requests

init_currency = input ("Enter initial currency:").upper()
target_currency = input ("Enter target currency:").upper()

while True:
    try:
        amount = float(input("Enter amount to convert: "))
    except ValueError:
        print("The amount must be a number")
        continue
    if amount <= 0:
        print("The amount must be greater than 0")
        continue
    else:
        break
    

url = f"https://api.apilayer.com/fixer/convert?to={init_currency}&from={target_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "Tpnb1VT67Il5TvJdwjZQBohb8enlfHH2"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
if response.status_code != 200:
    print(f"Status code: {response.status_code}\nThere was a problem with the request. Try again later.")
    quit()
else:
    result = response.json()
    if result.get("success"):
        print(result)
        print(f"{amount} {init_currency} = {response.text} {target_currency}")
    else:
        print(f"Error: {result.get('error', {}).get('info')}")