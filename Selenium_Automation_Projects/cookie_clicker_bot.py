import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("YOUR CHROME DRIVER PATH")
driver = webdriver.Chrome(service=service)

# Open the Cookie Clicker game
driver.get('http://orteil.dashnet.org/experiments/cookie/')

# Locate the cookie element
game = driver.find_element(By.ID, 'cookie')

# Define a loop for clicking the cookie and making purchases
for _ in range(300):
    # Click the cookie
    game.click()

    try:
        # Re-locate `cursor` and `grandma` elements dynamically
        cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')
        grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')

        # Check if they are clickable by inspecting their class or other attributes
        if "enabled" in cursor.get_attribute("class"):
            cursor.click()
        if "enabled" in grandma.get_attribute("class"):
            grandma.click()
    except Exception as e:
        # Handle any exceptions (like stale element) and continue
        print(f"Error occurred: {e}")

# Print the cookies per second value
cookies_per_sec = driver.find_element(By.XPATH, '//*[@id="cps"]').text
print(f"Cookies per second: {cookies_per_sec}")

# Sleep to observe the browser before closing
time.sleep(30)
driver.quit()
