from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\\Development\\chromedriver.exe") # YOUR CHROME DRIVER PATH
driver = webdriver.Chrome(service=service)
driver.get('https://www.amazon.com/ref=nav_logo')
links = driver.find_elements(By.CSS_SELECTOR, '.navAccessibility a')
link_names = []
for link in links:
    link_names.append(link.text)
for l in link_names:
    print(l)
