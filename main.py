#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
dm = DataManager()
from notification_manager import NotificationManager
# dm.add_city("Delhi", "GAU", 64)
# print(dm.get_data())
# fs = FlightSearch()
# print((fs.check("BOM", "GAU", "20/7/2023", "21/7/2023", 64)))

fd = FlightData()

x = fd.avail_offers()
print(x)

if x != []:
    nm = NotificationManager()
    nm.send_sms(x)

