# required imports
import requests
import os

# fetching the environment variables
API_KEY = os.environ.get('API_AUTH_KEY')

print(API_KEY)

ENVIRONMENT = os.environ.get('PYTHON_ENV')

# defining mock data
mock_data = {"rates": {
    "AED": 4.188393,
    "AFN": 119.478416,
    "ALL": 122.218232,
    "AMD": 548.237477,
    "ANG": 2.054213,
    "CHF": 1.042796,
    "CLF": 0.033991,
    "CLP": 937.926506,
    "CNY": 7.241387,
    "COP": 4569.22612,
    "CRC": 723.403315}}


def less_than_ten():
    # url for the API
    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}"

    if ENVIRONMENT == 'Production':
        # fetching the API data via GET method
        r = requests.get(url)
        # converting response to json
        raw_json = r.json()
    else:
        # setting the mock data as rates
        raw_json = mock_data
    
    rates = raw_json["rates"]  # fetching rates
    return filter_rates(rates)

def filter_rates(rates):
    return {key:value for (key,value) in rates.items() if value<10}