import requests


# This class is responsible for talking to the Google Sheet.
class DataManager:
    # Define the endpoints for Sheety and the Flight Deals spreadsheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co"
        self.flightdeals_endpoint = f"{self.sheety_endpoint}/ce74c6afdba031db0dcfb9868e6eafbb/flightDeals/prices"
        self.destination_data = ""

    # Takes all the data from the spreadsheet and returns it formatted.
    def get_info(self):
        response = requests.get(url=self.flightdeals_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # Updates a given row on the sheet by adding the IATA code supplied.
    def update_sheet(self, iata:str, row_id:str):
        update_endpoint = f"{self.flightdeals_endpoint}/{row_id}"
        parameters = {
            "price" : {
                "iataCode" : iata
            }
        }
        response = requests.put(url=update_endpoint, json=parameters)
        print(response)