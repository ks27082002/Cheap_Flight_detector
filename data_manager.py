import requests
SHEETY_API = "https://api.sheety.co/8733df2434363dff6967d520106ad4a2/copyOfFlightDeals/prices"
class DataManager:

    def add_city(self, city, iata_code, price):
        body = {
            "price": {
                "city": city,
                "iataCode": iata_code,
                "lowestPrice": price
            }
        }
        header = {
            "Content-Type": "application/json"
        }
        response = requests.post(url=SHEETY_API, json=body, headers=header)
        print(response.status_code)
    def get_data(self):
        response = requests.get(url=SHEETY_API)
        return response.json()
