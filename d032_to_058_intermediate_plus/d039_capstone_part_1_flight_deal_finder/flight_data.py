# This class is responsible for structuring the flight data.
class FlightData:
    def __init__(self, price, origin, destination, depart_date, return_date):
        """Constructor for initializing a new flight data instance with specific travel details."""
        self.price = price
        self.origin = origin
        self.destination = destination
        self.depart_date = depart_date
        self.return_date = return_date

def find_cheapest_flight(data):
    # Data from the first flight in the json data.
    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]

    # Initialize FlightDatawith the first flight, for comparison.
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["arrival"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is {lowest_price}")

    return cheapest_flight