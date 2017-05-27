#coding:utf-8
from selenium import webdriver 
import location

def login(driver):
	driver.maximize_window()
	findXpath('//*[@id="userNmae"]/input').clear()
	findXpath('//*[@id="userNmae"]/input').send_keys('testuser')
	findXpath('//*[@id="password"]/input').clear()
	findXpath('//*[@id="password"]/input').send_keys('aa123456')
	findXpath('//*[@id="btn"]/span').click()

def login_input(driver, username, password):
	driver.maximize_window()
	findXpath('//*[@id="userNmae"]/input').clear()
	findXpath('//*[@id="userNmae"]/input').send_keys(usernmae)
	findXpath('//*[@id="password"]/input').clear()
	findXpath('//*[@id="password"]/input').send_keys(password)
	findXpath('//*[@id="btn"]/span').click()
	