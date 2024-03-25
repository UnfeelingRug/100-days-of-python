import smtplib
from email.mime.text import MIMEText
from requests import get

# Defining desired stock, company name, and my API Key for AlphaVantage.
STOCK = "TSLA"
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_API_KEY = 'REDACTED'
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
NEWS_API_KEY = 'REDACTED'

my_email = 'REDACTED'
password = 'REDACTED'


# Gets the stock prices for the requested stock, moving on to check the news if the stock went up or down >5%.
def get_stock_price(stock):
    parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': stock,
        'apikey': STOCK_API_KEY,
    }
    response = get(STOCK_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()['Time Series (Daily)']
    data_list = [value for (key, value) in data.items()]

    yesterday_close = float(data_list[0]['4. close'])
    daybefore_close = float(data_list[1]['4. close'])
    difference = yesterday_close - daybefore_close
    diff_percent = abs(difference / daybefore_close) * 100

    if diff_percent > 10:
        if difference > 0:
            return '🔺', round(abs(difference), 2)
        else:
            return '🔻', round(abs(difference), 2)


# Gets the news ticker info for the requested company, searching based on relevancy.
def get_news(company):
    parameters = {
        'qInTitle': company,
        'language': 'en',
        'sortBy': 'relevancy',
        'pageSize': 3,
        'apiKey': NEWS_API_KEY,
    }
    response = get(NEWS_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()['articles']

    report = f'''\
<html>
    <body>
        <p style="font-size: 15px; margin-bottom: 0px;"><b>{data[0]['title']}</b></p>
        <p style="font-size: 14px; margin-top: 0px; margin-left: 20px">{data[0]['description']}</p>
        <p style="font-size: 15px; margin-bottom: 0px;"><b>{data[1]['title']}</b></p>
        <p style="font-size: 14px; margin-top: 0px; margin-left: 20px">{data[1]['description']}</p>
        <p style="font-size: 15px; margin-bottom: 0px;"><b>{data[2]['title']}</b></p>
        <p style="font-size: 14px; margin-top: 0px; margin-left: 20px">{data[2]['description']}</p>
    </body>
</html>
'''
    return report


def send_email(report, direction, difference):
    message = MIMEText(report, 'html')
    message['Subject'] = f'{STOCK}{direction}{difference}%'

    with smtplib.SMTP('smtp-mail.outlook.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=message.as_string()
        )


mvmt, diff = get_stock_price(STOCK)
if mvmt == '🔺' or  mvmt == '🔻':
    send_email(get_news(COMPANY_NAME), mvmt, diff)
    print('Success!~')