import datetime
import pandas
import smtplib
from email.mime.text import MIMEText
from random import randint

my_email = 'REDACTED'
password = 'REDACTED'
now = datetime.datetime.now()

data = pandas.read_csv('birthdays.csv')
birthdays = data.to_dict(orient='records')

for person in birthdays:
    if person['month'] == now.month and person['day'] == now.day:
        filepath = f'letter_templates/letter_{randint(1,3)}.txt'
        with open(filepath) as f:
            letter = f.read().replace('[NAME]', person['name'])
        message = MIMEText(letter)
        message['Subject'] = 'Happy Birthday!'

        with smtplib.SMTP('smtp-mail.outlook.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='REDACTED',
                msg=message.as_string()
            )
