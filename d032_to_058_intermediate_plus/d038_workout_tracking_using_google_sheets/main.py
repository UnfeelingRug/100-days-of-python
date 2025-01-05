import requests
from datetime import datetime

# Nutritionix API credentials.
APP_ID = "REDACTED"
API_KEY = "REDACTED"

# Nutritionix domain, endpoint, and connection information.
nut_domain = "https://trackapi.nutritionix.com"
nlfe_endpoint = f"{nut_domain}/v2/natural/exercise"
headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

#Sheety domain and endpoint information.
sht_domain = "https://api.sheety.co"
workout_endpoint = f"{sht_domain}/REDACTED"

# Personal info.
AGE = 27
HEIGHT = 183
WEIGHT_LBS = 223.1
WEIGHT_KG = round(WEIGHT_LBS / 2.20462, 1)

# Get the exercise info from the user, compile it into a request and send it to the server.
exercise = input("How did you exercise? ")
parameters = {
    "query" : exercise,
    "age" : AGE,
    "height_cm" : HEIGHT,
    "weight_kg" : WEIGHT_KG,
}
response = requests.post(url=nlfe_endpoint, json=parameters, headers=headers)
result = response.json()

#Get the current date and time for sending information to the Google Sheet.
date = datetime.now().strftime("%Y/%m/%d")
time = datetime.now().strftime("%I:%M")

# Log individual exercises to the sheet by sending them to Sheety.
for i in result['exercises']:
    parameters = {
        "workout" : {
            "date" : date,
            "time" : time,
            "exercise" : i["name"].title(),
            "duration" : i["duration_min"],
            "calories" : i["nf_calories"],
        }
    }
    response = requests.post(url=workout_endpoint, json=parameters)
    print(response.text)