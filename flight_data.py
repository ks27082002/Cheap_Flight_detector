from flight_search import FlightSearch
from data_manager import DataManager
from datetime import date
from dateutil.relativedelta import relativedelta
class FlightData:
    def __init__(self):
        self.dm = DataManager()
        self.fs = FlightSearch()
        self.today = date.today().strftime("%d/%m/%Y")
        self.later = (date.today() + relativedelta(months=+6)).strftime("%d/%m/%Y")
    def avail_offers(self):
        print(self.today, self.later)
        destination_data = self.dm.get_data()
        destination_data = destination_data["prices"]
        offers = []
        for item in destination_data:
            print("BOM", item["iataCode"], str(self.today), str(self.later), item["lowestPrice"])
            flight_data = self.fs.check("BOM", item["iataCode"], str(self.today), str(self.later), item["lowestPrice"])
            print(flight_data)
            flight_data = flight_data['data']
            for offer in flight_data:
                offers.append({})
                offers[-1]["cityTo"] = offer["cityTo"]
                offers[-1]["price"] = offer["price"]
                offers[-1]["airlines"] = offer["airlines"]
                offers[-1]['deep_link'] = offer['deep_link']

        return offers




