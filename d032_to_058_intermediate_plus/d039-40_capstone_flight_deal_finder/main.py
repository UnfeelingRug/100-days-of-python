# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# Import required modules.
import time
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

# ========== Set up Flight Search and Data Manager ==========
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_info()

ORIGIN_CITY_IATA = "LON"

# ========== Search for Flights ==========
tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    print(f"Getting flights for {destination["city"]}...")
    flights = flight_search.find_flight(ORIGIN_CITY_IATA, destination["iataCode"], from_time=tomorrow, to_time=six_months)
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination["city"]}: {cheapest_flight.price}")
    time.sleep(2)