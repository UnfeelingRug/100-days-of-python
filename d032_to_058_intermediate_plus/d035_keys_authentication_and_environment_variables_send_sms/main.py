import requests
from twilio.rest import Client


# This function will call the OpenWeather API for their One-Call forecast, and return it as a dictionary.
def get_weather() -> dict:
    parameters = {
        'lat': 45,
        'lon': -80,
        'appid': 'REDACTED',
    }
    response = requests.get(url='https://api.openweathermap.org/data/2.8/onecall', params=parameters)
    response.raise_for_status()
    return response.json()


# This function will check the hourly forecast for the next 12 hours, checking if any hour forecasts for precipitation.
def check_for_rain(weather: dict) -> bool:
    for x in weather['hourly'][0:12]:
        for y in x['weather']:
            if y['id'] < 700:
                return True
    return False


# This function will log in to the Twilio API and send a text to the specified number with a given message.
def notify_user(message: str):
    account_sid = 'REDACTED'
    auth_token = 'REDACTED'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+REDACTED',
        body=message,
        to='REDACTED'
    )
    print(message.status)


# Call for the forecast, check the next twelve hours for precipitation of any kind, and inform the user of the result.
if check_for_rain(get_weather()):
    notify_user('Precipitation is expected within the next twelve hours - bring an umbrella!')
else:
    print('No precipitation is forecast within the next twelve hours. You can head out unburdened by umbrellas!')
