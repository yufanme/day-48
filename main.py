from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/WilliamYu/Development/chromedriver"

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)
# driver.get("https://www.amazon.com")
# driver.close()

# driver.get("https://www.amazon.com/Kindle-Paperwhite-Waterproof-International/dp/B07741S7Y8/ref=sr_1_2?crid=3MO08AY697FAM&keywords=kindle+paperwhite&qid=1644749815&sprefix=kindle%2Caps%2C355&sr=8-2")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)
#
# driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# doc_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(doc_link.text)
#
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
# print(bug_link.get_attribute("href"))
#
# driver.quit()

# challenge 1
# driver.get("https://www.python.org/")
# way 1
# dates = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/time')
# activities = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li/a')
#
# content = {}
# for index in range(len(dates)):
#     content[index] = {"time": dates[index].text, "name": activities[index].text}
# print(content)

# way 2
# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for time in event_times:
#     print(time.text)
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# for name in event_names:
#     print(name.text)
#
# event = {index: {"time": event_times[index].text, "name": event_names[index].text} for index in range(len(event_times))}
# print(event)
# driver.quit()
