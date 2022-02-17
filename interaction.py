from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_driver_path = "/Users/WilliamYu/Development/chromedriver"
service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service)

# learn click and input by selenium
# driver.get(URL)
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# print(article_count.text)
#
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

# fake sign in app brewery
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("F")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Y")
email = driver.find_element(By.NAME, "email")
email.send_keys("888@gmail.com")
sign_up_button = driver.find_element(By.CSS_SELECTOR, "button")
sign_up_button.click()
# driver.quit()
