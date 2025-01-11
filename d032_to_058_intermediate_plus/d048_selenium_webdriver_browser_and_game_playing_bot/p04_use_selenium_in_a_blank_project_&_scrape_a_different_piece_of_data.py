# Import required modules.
from selenium import webdriver
from selenium.webdriver.common.by import By

# Add settings to keep Chrome open after program finishes.
# Once that's done, open Chrome and navigate to the desired site.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find the list of elements matching the requested criteria.
# In this case, the listed counts of "Active Editors" and "Articles in English"
stats = driver.find_elements(By.CSS_SELECTOR, value="#articlecount ul li")

# Split up the strings to find which one has the article count.
# Do some processing on the raw text to turn the number into an int, and print.
for i in stats:
    words = i.text.split()
    if "articles" in words:
        number = int("".join(words[0].split(",")))
        print(number)

# Close the browser and end the program.
driver.quit()