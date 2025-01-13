# Import required modules.
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def format_price(data: str) -> str:
    """Takes a price as formatted by the mock site, then returns it reformatted."""
    # Strip off white space from the start and end of the string, and remove the dollar sign.
    s1 = data.strip().split("$")[1]
    # Remove the "+", "/mo", and any information following them, if present.
    s2 = s1.split("/")[0].split("+")[0]
    # Remove the comma from the price.
    s3 = "".join(s2.split(","))
    return s3


def format_address(data: str) -> str:
    """Takes an address as formatted by the mock site, and returns it formatted more simply."""
    # Strip off white space from the start and end of the string. Split on the pipe.
    s1 = data.split("|")[-1].strip()
    # Split on commas and restructure to remove repeats of the address. Strip white space.
    s2 = ",".join(s1.split(",")[-3:]).strip()
    # Split up s3 and search for postal codes. If they are included, remove them.
    s3 = s2.split()
    if len(s3[-1]) == 5:
        s3.pop(-1)
    # Re-join everything for final format, then return.
    s4 = " ".join(s3)
    return s4


zillow_endpoint = "https://appbrewery.github.io/Zillow-Clone/"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

# Get the website data from the Zillow Clone website, save to a variable, and soup it.
response = requests.get(url=zillow_endpoint, headers=headers)
zillow_site = response.text
soup = BeautifulSoup(zillow_site, "html.parser")

# Find all the posts on the given page, and save them to a dictionary with price, address, and link.
posts = soup.select(selector=".StyledPropertyCardDataWrapper")
listings = []
for post in posts:
    listings.append({
        "price": format_price(post.find(class_="PropertyCardWrapper").text),
        "address": format_address(post.find(name="address").text),
        "link": format_address(post.find(class_="StyledPropertyCardDataArea-anchor").get("href")),
    })

# Add settings to keep Chrome open after program finishes.
# Once that's done, open Chrome and navigate to the desired site.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("REDACTED")

# For every listing, input the info to the Google Form, then submit and loop.
for i in listings:
    sleep(1)
    input_boxes = driver.find_elements(By.CLASS_NAME, value="whsOnd")
    address_input = input_boxes[0]
    price_input = input_boxes[1]
    link_input = input_boxes[2]
    submit = driver.find_element(By.CLASS_NAME, value="uArJ5e")
    address_input.send_keys(i["address"])
    price_input.send_keys(i["price"])
    link_input.send_keys(i["link"])
    submit.click()
    return_link = driver.find_element(By.LINK_TEXT, value="Submit another response")
    return_link.click()