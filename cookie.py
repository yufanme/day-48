from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# todo 1 initialize webdriver.
chrome_driver_path = "/Users/WilliamYu/Development/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# todo 2 open the web
URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)
cookie = driver.find_element(By.ID, "cookie")

# todo 3 take action
# todo 3.1 click the cookie for 5 minutes
timeout = time.time() + 5
five_min = time.time() + 5 * 60

while True:
    cookie.click()
    # todo 3.2 every 5 seconds, buy the most expensive add on on the right top
    if time.time() > timeout:
        # todo 3.2.1 collect all items that can buy
        all_items = driver.find_elements(By.CSS_SELECTOR, "#store b")
        all_price = []
        for item in all_items:
            if item.text != "":
                all_price.append(int(item.text.split("-")[1].strip().replace(",", "")))
        # print(all_price)
        # todo 3.2.2 get the money that now
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        # print(money)
        # todo 3.3.3 get the most expensive good that can buy
        most_expensive_index = 0
        for index in range(len(all_price)):
            if money > all_price[index]:
                most_expensive_index = index
        # todo 3.3.4 click the most expensive good
        all_items[most_expensive_index].click()
        timeout = time.time() + 5
    # todo 3.3 after 5 minutes, check the cookie/second to see the amount of cookie
    if time.time() > five_min:
        cookie_second = driver.find_element(By.ID, "cps")
        print(cookie_second.text)
        break

# todo 3.4 quit the browser
driver.quit()


