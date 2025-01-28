import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\Development\chromedriver.exe") # your chrome driver path
driver = webdriver.Chrome(service=service)

driver.get(
    'https://www.linkedin.com/checkpoint/lg/sign-in-another-account')
fname = driver.find_element(By.XPATH, '//*[@id="username"]')
fname.send_keys('YOUR EMAIL ID  ')
email = driver.find_element(By.XPATH, '//*[@id="password"]')
email.send_keys('YOUR PASSWORD')
login = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login.click()
time.sleep(30)
