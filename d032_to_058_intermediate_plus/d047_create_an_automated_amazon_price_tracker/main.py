# Import required modules.
import requests
from bs4 import BeautifulSoup

def check_price(product, url, target_price=0):
    """Scrapes the given URL to find the price of the product."""
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Accept-Language" : "en-CA,en-US;q=0.7,en;q=0.3",
    }
    response = requests.get(url=url, headers=headers)
    store_page = response.text
    soup = BeautifulSoup(store_page, "html.parser")
    price_whole = soup.find(name="span", class_="a-price-whole")
    price_decimal = soup.find(name="span", class_="a-price-fraction")
    price_full = float(price_whole.getText()+price_decimal.getText())

    if price_full < target_price:
        notify_user(product, url, price_full)


def notify_user(product, url, price):
    """Lets the user know that a given product is below the target price.
    If I wanted to make this into a full product, this would email or text the user."""
    print(f"{product} is below your target price, now at ${price}! {url}")


# Check the price of the Pressure Cooker on the mock Amazon site, for testing.
check_price(product="Instant Pot Pressure Cooker",
            url="https://appbrewery.github.io/instant_pot/",
            target_price = 100)