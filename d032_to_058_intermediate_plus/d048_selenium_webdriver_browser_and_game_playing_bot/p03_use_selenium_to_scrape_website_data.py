# Import required modules.
from selenium import webdriver
from selenium.webdriver.common.by import By

# Add settings to keep Chrome open after program finishes.
# Once that's done, open Chrome and navigate to the desired site.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# Find the list of elements matching the requested criteria.
# In this case, the five events listed under "Upcoming Events" on the Python site.
upcoming_events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div ul li")

# For each event, find the link and separate the date from the event name.
# Then print the whole thing, nicely formatted on one line each.
for i in upcoming_events:
    link = i.find_element(By.CSS_SELECTOR, value="a").get_attribute("href")
    event = i.text.split("\n")
    print(f'{event[0]} | {event[1]} - {link}')

# Close the browser and end the program.
driver.quit()