# Import required modules.
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Add settings to keep Chrome open after program finishes.
# Once that's done, open Chrome and navigate to the desired site.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# Find the desired elements and enter the required data, then submit.
first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Tony")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Stark")
email = driver.find_element(By.NAME, value="email")
email.send_keys("iron-man@marvel.com")

# You can submit one of two ways:
# Send an ENTER keypress to one of the text input boxes.
if randint(0, 1) == 0:
    email.send_keys(Keys.ENTER)
# Or find the "Sign Up" buttom by some identifier and send a click event.
else:
    sign_up = driver.find_element(By.CLASS_NAME, value="btn")
    sign_up.click()

# Close the browser and the program.
# driver.close()