from selenium import webdriver
import time

url ='http://www.baidu.com'
driver = webdriver.Firefox()
driver.get(url)
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(3)
driver.quit()
