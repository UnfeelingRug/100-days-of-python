# A basic Cookie-Clicker player bot. Plays a simple loop.
# Auto-clicks the big cookie, checks for affordable upgrades next.
# Finally, buys the latest affordable building.

# Import required modules.
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


def cookie_count() -> int:
    """Returns the current number of cookies as an integer."""
    cookie_counter = driver.find_element(By.CSS_SELECTOR, value="#cookies")
    cookies = number_format(cookie_counter.text.split()[0])
    return cookies


def number_format(original: str) -> int:
    """When given a number, changes it from a string to an int.
    Does some processing depending on how the number is presented."""
    if "e" in original:
        pass
    elif "," in original:
        return int("".join(original.split(",")))
    else:
        return int(original)
    return 0


def click_cookie(x: int):
    """Clicks the big cookie a defined number of times."""
    big_cookie = driver.find_element(By.ID, value="bigCookie")
    for i in range(x):
        big_cookie.click()
        sleep(0.1)


def check_upgrades():
    upgrades_bar = driver.find_element(By.ID, value="upgrades")
    upgrades = upgrades_bar.find_elements(By.CLASS_NAME, value="enabled")
    for upgrade in upgrades:
        cookies = cookie_count()
        action.move_to_element(upgrade)
        action.perform()
        listed_price = driver.find_element(By.CSS_SELECTOR, value="#tooltip div .price").text
        price = number_format(listed_price)
        if cookies - price >= 0:
            upgrade.click()


def check_buildings():
    buildings_bar = driver.find_element(By.ID, value="products")
    buildings = buildings_bar.find_elements(By.CLASS_NAME, value="unlocked")
    for i in range(len(buildings)):
        building = buildings[-i-1]
        cookies = cookie_count()
        listed_price = building.find_element(By.CLASS_NAME, value="price").text
        price = number_format(listed_price)
        if cookies - price >= 0:
            building.click()


# Add settings to keep Chrome open after program finishes.
# Once that's done, open Chrome and navigate to the desired site.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-data-dir=/selenium")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
action = ActionChains(driver)

# Manufactured delay to let the game load.
# Once prepared, unleash hell.
sleep(2)

while True:
    click_cookie(15)
    check_upgrades()
    check_buildings()
