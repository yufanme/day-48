from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://orteil.dashnet.org/cookieclicker/"
chrome_driver_path = "/Users/WilliamYu/Development/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(URL)
cookie = driver.find_element(By.ID, "bigCookie")

time_start = time.time()
time_out = 400
while time.time() < time_start + time_out:
    cookie.click()


