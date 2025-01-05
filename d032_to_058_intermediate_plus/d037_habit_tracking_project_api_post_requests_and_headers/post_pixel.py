# Important packages, needed for the project.
import requests
from datetime import datetime

# User info.
USERNAME = "unfeelingrug"
TOKEN = "REDACTED"

# Defining the endpoints to which we'll send all of our data.
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Setting up the header so info can be changed on my account.
headers = {
    "X-USER-TOKEN" : TOKEN
}

# Function to take information and send a pixel to Pixela for tracking.
def send_pixel(destination: str, quantity: str):
    # Get today's date, format it in the proper way for Pixela to accept.
    # Ex. January 5, 2025 would format as "20250105", yyyyMMdd
    today = datetime.now().strftime("%Y%m%d")

    # Defining info for the pixel to be sent to the site.
    pixel = {
        "date" : today,
        "quantity" : quantity,
    }

    # Sending the POST request to the server with the info, returning response.
    response = requests.post(url=destination, json=pixel, headers=headers)
    print(response.text)


# Continuously ask until the user provides a valid input.
while True:
    # Check which graph the user wants to update.
    graph = input("1. Programming Practice\n"
                  "Which graph would you like to send a pixel for? ")

    # Ask a context-dependent question based on their response.
    if graph == "1":
        destination = f"{graph_endpoint}/graph{graph}"
        quantity = input("How many minutes did you spend programming? ")
        send_pixel(destination, quantity)
        break