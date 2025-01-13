# Import required modules.
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Add settings to keep Chrome open after program finishes.
# Once that's done, open Chrome and navigate to the desired site.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://fast.com/")

# Wait for the speed test to complete, then fetch the measured speed and units.
sleep(15)
speed = float(driver.find_element(By.ID, value="speed-value").text)
units = driver.find_element(By.ID, value="speed-units").text

# If the units are in Gbps, multiply the result by 1000. Convert to int.
if units == "Gbps":
    speed = int(speed*1000)
elif units == "Mbps":
    speed = int(speed)
    
# Print the expected, actual, and difference. Note the final result.
print(f"Target: 1000Mbps | Actual: {speed}Mbps | Difference: {speed-1000}Mpbs")
if speed-1000 < 0:
    print("Speed is lower than expected!")
elif speed-1000 == 0:
    print("Speed is exactly what was advertised!")
else:
    print("Speed is faster than expected!")