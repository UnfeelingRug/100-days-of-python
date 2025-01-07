import os
import requests
from dotenv import load_dotenv

# This class is responsible for talking to the Amadeus Flight Search API.
class FlightSearch:
    # Initialize environment variables and set up the endpoints for requests.
    def __init__(self):
        load_dotenv()
        self.citysearch_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.flightsearch_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self._api_key = os.getenv("AM_API_KEY")
        self._api_secret = os.getenv("AM_API_SECRET")
        self.token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self._token = self._get_new_token()


    def _get_new_token(self):
        """Generates a token for Amadeus using the user's API Key+Secret from the environment variables.
           Runs automatically during initialization, should never need to be called manually."""
        # Define the headers and body required for the POST request.
        headers = {"Content-Type" : "application/x-www-form-urlencoded"}
        body = {
            "grant_type" : "client_credentials",
            "client_id" : self._api_key,
            "client_secret" : self._api_secret,
        }

        # Sends the POST request to the server, informs the user of their token and its expected expiry.
        response = requests.post(url=self.token_endpoint, headers=headers, data=body)
        print(f"Your token is {response.json()['access_token']}.")
        print(f"Your token expires in {response.json()['expires_in']} seconds.")
        return response.json()['access_token']

    def find_iata(self, destination:str) -> str:
        """Returns the IATA Code of the given destination."""
        headers = {"Authorization" : f"Bearer {self._token}"}
        parameters = {
            "keyword" : destination,
            "max" : "2",
            "include" : "AIRPORTS",
        }
        response = requests.get(url=self.citysearch_endpoint, headers=headers, params=parameters)
        return response.json()["data"][0]["iataCode"]

    def find_flight(self, origin, destination, from_time, to_time):
        """Searches for flights between two cities on specified departure/return dates using Amadeus API."""
        headers = {"Authorization" : f"Bearer {self._token}"}
        parameters = {
            "originLocationCode" : origin,
            "destinationLocationCode" : destination,
            "departureDate" : from_time.strftime("%Y-%m-%d"),
            "returnDate" : to_time.strftime("%Y-%m-%d"),
            "adults" : 1,
            "nonStop" : "true",
            "currencyCode" : "GBP",
            "max" : "10",
        }
        response = requests.get(url=self.flightsearch_endpoint, headers=headers, params=parameters)
        return response.json()