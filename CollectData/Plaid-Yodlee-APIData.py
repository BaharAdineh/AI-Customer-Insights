import requests
import json

# Replace YOUR_PUBLIC_KEY with your actual Plaid API public key
PLAID_PUBLIC_KEY = 'YOUR_PUBLIC_KEY'

# Endpoint for retrieving transactions
TRANSACTIONS_ENDPOINT = 'https://sandbox.plaid.com/transactions/get'

# Example access_token for a Plaid Link-generated access token
ACCESS_TOKEN = 'access-sandbox-8c15b71a-5551-4b3a-92c8-9e9b928a2b35'

# Request data for retrieving transactions
data = {
    "client_id": PLAID_PUBLIC_KEY,
    "secret": PLAID_PUBLIC_KEY,
    "access_token": ACCESS_TOKEN
}

# Send request to Plaid API
response = requests.post(TRANSACTIONS_ENDPOINT, json=data)

# Check if request was successful
if response.status_code == 200:
    # Parse response data
    transactions = json.loads(response.text)
    # Print transactions
    print(transactions)
else:
    # Print error message
    print(f'Failed to retrieve transactions: {response.text}')
