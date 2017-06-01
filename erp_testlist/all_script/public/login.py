#coding:utf-8
from selenium import webdriver

def login(driver):
	driver.maximize_window()
	driver.find_element_by_xpath('//*[@id="userNmae"]/input').clear()
	driver.find_element_by_xpath('//*[@id="userNmae"]/input').send_keys('testuser')
	driver.find_element_by_xpath('//*[@id="password"]/input').clear()
	driver.find_element_by_xpath('//*[@id="password"]/input').send_keys('aa123456')
	driver.find_element_by_xpath('//*[@id="btn"]/span').click()

def login_input(driver, username, password):
	driver.maximize_window()
	driver.find_element_by_xpath('//*[@id="userNmae"]/input').clear()
	driver.find_element_by_xpath('//*[@id="userNmae"]/input').send_keys(usernmae)
	driver.find_element_by_xpath('//*[@id="password"]/input').clear()
	driver.find_element_by_xpath('//*[@id="password"]/input').send_keys(password)
	driver.find_element_by_xpath('//*[@id="btn"]/span').click()
	