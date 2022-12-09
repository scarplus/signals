## dont forget to go and cancel the trade from your account after running this program.
# this program will help place a buy order of 15 APPL stocks in your tda account



import requests

accountnumber='you tda actual account number'
bearer_token='Your_bearer_token_key'

# define the url
url = f'https://api.tdameritrade.com/v1/accounts/{accountnumber}/orders'

# define the payload
payload = {
  "orderType": "MARKET",
  "session": "NORMAL",
  "duration": "DAY",
  "orderStrategyType": "SINGLE",
  "orderLegCollection": [
    {
      "instruction": "Buy",
      "quantity": 15,
      "instrument": {
        "symbol": "AAPL",
        "assetType": "EQUITY"
      }
    }
  ]
}
	
Bearer_Token='Bearer '+bearer_token
# set the headers
headers = {
    'Authorization': Bearer_Token
}

# make the request
r = requests.post(url=url, json=payload, headers=headers)

print (r)

# r value of 201 is success order placement
