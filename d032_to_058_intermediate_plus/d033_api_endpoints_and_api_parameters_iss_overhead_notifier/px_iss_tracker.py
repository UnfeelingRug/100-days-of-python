import requests
import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText

# Setting my latitude and longitude, getting the current datetime, and setting email login info.
MY_LAT = 45
MY_LNG = -75
NOW = datetime.now()
email = 'REDACTED'
password = 'REDACTED'


# Defining and sending the email, for use once the ISS is confirmed to be overhead.
def send_email():
    # Email format for notification of ISS tracking.
    message = MIMEText('The International Space Station should be passing overhead right now!\n'
                       'If you head outside, you may be able to spot it!')
    message['Subject'] = 'Damien - look up!'
    with smtplib.SMTP('smtp-mail.outlook.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=message.as_string()
        )


# Make an API request to open-notify to obtain the ISS' current latitude and longitude.
# Compare that with my own latitude and longitude, and return True if it is within 5 degrees of my location.
def is_iss_overhead():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    if ((MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5)) and ((MY_LNG - 5) <= iss_longitude <= (MY_LNG + 5)):
        return True
    else:
        return False


# Make an API request to sunrise-sunset to get my local sunrise and sunset times. Format the hours as integers.
# If the current hour is before the sunrise hour or after the sunset hour, return True. Otherwise, False.
def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    if (sunrise > NOW.hour) or (sunset < NOW.hour):
        return True
    else:
        return False


# If the time is before sunrise or after sunset, and the ISS is visible from my position (within 5 degrees), notify me.
# Otherwise, tell me why it isn't. Loop through this every 60 seconds until an email is sent, or I close the program.
while True:
    if is_night() and is_iss_overhead():
        print('If the skies are clear, the ISS should be visible overhead!')
        send_email()
        break
    elif is_night() and not is_iss_overhead():
        print('The ISS is not visible overhead.')
    elif not is_night() and is_iss_overhead():
        print('The ISS is overhead, but it is too bright out to see it!')
    elif not is_night() and not is_iss_overhead():
        print('The ISS is not overhead, but it would be too bright out to see it anyway!')
    time.sleep(60)