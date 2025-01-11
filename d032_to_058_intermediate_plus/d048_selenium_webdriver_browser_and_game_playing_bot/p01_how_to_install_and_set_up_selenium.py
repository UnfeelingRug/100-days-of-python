# Import required modules.
from selenium import webdriver

# Add settings to keep Chrome open after program finishes.
# Once that's done, open Chrome and navigate to the desired site.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

# Closes both the browser and the program.
driver.quit()