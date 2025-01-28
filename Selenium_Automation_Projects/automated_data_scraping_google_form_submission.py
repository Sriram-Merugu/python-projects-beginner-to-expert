from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import random

# Configure Selenium WebDriver
service = Service("C:/Development/chromedriver.exe")  # Replace with your ChromeDriver path
driver = webdriver.Chrome(service=service)

# Google Form URL
google_form_url = "YOUR GOOGLE FORM URL"

# Hacker News URL
hacker_news_url = "https://news.ycombinator.com/"

# Headers for requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Scrape data from Hacker News
def scrape_hacker_news():
    response = requests.get(hacker_news_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = []
    links = []
    points = []

    # Extract top stories
    for item in soup.select(".athing"):
        title = item.select_one(".titleline a").text
        link = item.select_one(".titleline a")["href"]
        point = item.find_next_sibling("tr").select_one(".score")
        point = point.text if point else "0 points"

        titles.append(title)
        links.append(link)
        points.append(point)

    return titles, links, points

# Fill Google Form with scraped data
def fill_google_form(titles, links, points):
    for i in range(len(titles)):
        driver.get(google_form_url)
        time.sleep(random.uniform(2, 4))  # Random delay to mimic human behavior

        try:
            # Fill the Title field
            title_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            title_input.send_keys(titles[i])

            # Fill the Link field
            link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input.send_keys(links[i])

            # Fill the Points field
            points_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            points_input.send_keys(points[i])

            # Submit the form
            submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit_button.click()

            print(f"Submitted: {titles[i]}")  # Debugging statement
            time.sleep(random.uniform(2, 4))  # Random delay between submissions

        except Exception as e:
            print(f"Error submitting form: {e}")

# Main function
def main():
    # Scrape data from Hacker News
    titles, links, points = scrape_hacker_news()

    # Fill Google Form with scraped data
    fill_google_form(titles, links, points)

    # Close the browser
    driver.quit()

# Run the script
if __name__ == "__main__":
    main()