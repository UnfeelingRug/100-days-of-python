# Import required modules.
from selenium import webdriver
from selenium.webdriver.common.by import By

# Add settings to keep Chrome open after program finishes.
# Once that's done, open Chrome and navigate to the desired site.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# You can find an element by name, and send text to an element that can accept it.
# You can also get attributes if you so desire.
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))
search_bar.send_keys("ayy lmao")

# You can also find an element by id, and check the size of said element.
submit_button = driver.find_element(By.ID, value="submit")
print(submit_button.size)

# You can find elements by their CSS selectors, and pull the links from anchor tags.
doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(doc_link.get_attribute("href"))

# You can find a link by searching the XPATH, and send click events.
guide_link = driver.find_element(By.XPATH, value="/html/body/div/div[3]/div/section/div[1]/div[1]/p[2]/a")
guide_link.click()

# Closes both the browser and the program.
# driver.quit()