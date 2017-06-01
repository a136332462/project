from selenium import webdriver
from public import login
from public import linkaddress
import time
login_url = linkaddress.link()
print(login_url)
driver = webdriver.Firefox()
driver.get(login_url)
login.login(driver)
time.sleep(2)
driver.quit()

