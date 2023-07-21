import requests
API_KEY = "wToeFxnzHISIMpB6Fcnpvuxe6x-8GFdD"
ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
class FlightSearch:
    def check(self, fly_from, fly_to, date_from, date_to, max_price):
        headers = {
            "apikey": API_KEY
        }
        parameters = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "price_to": max_price,
            "max_stopovers": 0
        }
        response = requests.get(url=ENDPOINT, headers=headers, params=parameters)
        print(response.status_code)
        return response.json()
