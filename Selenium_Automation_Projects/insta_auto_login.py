from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random

class InstagramFollowerBot:
    def __init__(self, path):
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation flag
        chrome_options.add_argument("--start-maximized")  # Start maximized to avoid detection
        chrome_options.add_argument("--disable-notifications")  # Disable notifications
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")  # Set user agent

        # Use Service object instead of executable_path
        service = Service(path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")

        # Wait for the login form to load
        wait = WebDriverWait(self.driver, 15)

        try:
            # Wait for the username and password fields to be present
            username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))

            # Fill in the login details
            username_field.send_keys(username)
            time.sleep(random.uniform(1, 2))  # Random delay to mimic human behavior
            password_field.send_keys(password)
            time.sleep(random.uniform(1, 2))

            # Click the login button
            login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
            login_button.click()

            # Wait for the home page to load (check for the Instagram logo)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Instagram"]')))
            print("Login successful!")

        except Exception as e:
            print(f"Error during login: {e}")
            raise

    def quit(self):
        self.driver.quit()


# Instantiate and run the bot
if __name__ == "__main__":
    # Replace with your Instagram credentials
    USERNAME = "your_instagram_username"
    PASSWORD = "your_instagram_password"

    # Path to your ChromeDriver
    CHROMEDRIVER_PATH = "C:/Development/chromedriver.exe"

    bot = InstagramFollowerBot(CHROMEDRIVER_PATH)
    try:
        bot.login(USERNAME, PASSWORD)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        bot.quit()