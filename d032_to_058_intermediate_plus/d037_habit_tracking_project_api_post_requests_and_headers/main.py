# Important packages, needed for the project.
import requests
from datetime import datetime

USERNAME = "unfeelingrug"
TOKEN = "REDACTED"

# Defining the endpoints to which we'll send all of our data.
pixela_endpoint = "https://pixe.la/v1/users"
userprofile_endpoint = f"https://pixe.la/@{USERNAME}"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pp_graph_endpoint = f"{graph_endpoint}/graph1"

# Defining user info for creating my account.
user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# Sending a post request to the server, creating a user account.
# Commented out because my account has already been created.
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

# Setting up the header so requests can be made to my account.
headers = {
    "X-USER-TOKEN" : TOKEN
}

# Defining the info for creating a new habit-tracker graph.
graph_config = {
    "id" : "graph1",
    "name" : "Programming Practice",
    "unit" : "Minutes",
    "type" : "int",
    "color" : "shibafu",
    "timezone" : "America/Toronto",
    "startOnMonday" : True,
}

# Creating a graph to track my programming practice habit.
# Commented out because the graph has already been created.
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

# Defining info for updating my profile.
profile_update = {
    "displayName" : "UnfeelingRug",
    "gravatarIconEmail" : "d-hill@live.ca",
    "timezone" : "America/Toronto",
    "pinnedGraphID" : "graph1",
}

# Sending the info to update my user profile.
# Commented out because my profile is now up-to-date.
#response = requests.put(url=userprofile_endpoint, json=profile_update, headers=headers)
#print(response.text)

# Get today's date, format it in the proper way for Pixela to accept.
# Ex. January 5, 2025 would format as "20250105", yyyyMMdd
today = datetime.now().strftime("%Y%m%d")

# Defining info for sending a pixel to the site.
pixel = {
    "date" : today,
    "quantity" : "60",
}

# Send a pixel to the site and post it.
response = requests.post(url=pp_graph_endpoint, json=pixel, headers=headers)
print(response.text)