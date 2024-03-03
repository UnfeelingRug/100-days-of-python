import datetime
import smtplib
from email.mime.text import MIMEText
from random import choice

# Set up the sender's email login, and get the current datetime.
my_email = 'REDACTED'
password = 'REDACTED'
now = datetime.datetime.now()

# Open the supplied quotes file, splitting it up into lines and separating the quote from the person who said it.
with open('quotes.txt') as f:
    messages = f.readlines()
    selection = choice(messages).split(' - ')

# If today is Monday, send out the chosen quote as an email to the listed recipient.
if now.weekday() == 0:
    message = MIMEText(f'{selection[0]}\n- {selection[1]}')
    message['Subject'] = 'Motivational Quote of the Day'

    with smtplib.SMTP('smtp-mail.outlook.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='REDACTED',
            msg=message.as_string()
        )
