#coding:utf-8
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, re, sys, unittest, os
sys.path.append('..')
from public import *
reload(sys)
sys.setdefaultencoding('utf8')

class Material_list(unittest.TestCase):

	'''物料列表'''
	def setUp(self):
		#参数设置
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.login_url = linkaddress.link()
		self.verificationErrors = []
		self.accept_alert_next = True
		name = '物料列表'
		print_path.print_path(name)   #文件输出路径

	def test_Page_skip(self):
		'''物料页面点击跳转'''
		print('%s  开始物料页面点击跳转测试' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time()))))
		driver = self.driver 
		driver.get(self.login_url)
		login.login(driver)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/div').click()   #点击物料
		time.sleep(1)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/ul/li[1]/div').click()   #点击物料管理
		time.sleep(1)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/ul/li[1]/ul/li[1]').click()   #点击物料列表
		time.sleep(1)
		click_page = location.findXpath(driver, '/html/body/div/div/div[2]/div/div[2]/section/div/div[2]/section/div[4]/div/ul/li[8]').text  #获取最后一页的值
		print('%s  获取最后一页的值值为:%s' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time())), click_page))
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[2]/section/div/div[2]/section/div[4]/div/ul/li[8]').click()  #点击最后一页跳转
		time.sleep(1)
		skip_page = location.findXpath(driver, '/html/body/div/div/div[2]/div/div[2]/section/div/div[2]/section/div[4]/div/span[3]/input').get_attribute('value')   #获取跳转后输入框的值
		print('%s  跳转后输入框的值为:%s' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time())), skip_page))
		self.assertEqual(click_page, skip_page, msg = '点击页面跳转失败，点击页面为%s，实际跳转页面为%s'%(click_page, skip_page))   #验证点击跳转的值域输入框的值是否相等
		print('%s  结束物料页面点击跳转测试' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time()))))

	def test_Input_skip(self):
		'''物料页面输入跳转'''
		print('%s  开始物料页面输入跳转测试' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time()))))
		driver = self.driver 
		driver.get(self.login_url)
		login.login(driver)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/div').click()   #点击物料
		time.sleep(1)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/ul/li[1]/div').click()   #点击物料管理
		time.sleep(1)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/ul/li[1]/ul/li[1]').click()   #点击物料列表
		time.sleep(1)
		input_page = 2   #设置输入框的值为2
		print('%s  设置输入框的值为:%s' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time())), input_page))
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[2]/section/div/div[2]/section/div[4]/div/span[3]/input').clear()   #清空输入框内文字
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[2]/section/div/div[2]/section/div[4]/div/span[3]/input').send_keys(input_page)   #将值输入到输入框内
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[2]/section/div/div[2]/section/div[4]/div/span[3]/input').send_keys(Keys.ENTER)   #按enter键跳转
		time.sleep(1)
		skip_page = location.findXpath(driver, '/html/body/div/div/div[2]/div/div[2]/section/div/div[2]/section/div[4]/div/ul/li[2]').text   #获取跳转后的页面的值
		print('%s  跳转后的页面的值为:%s' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time())), skip_page))
		self.assertEqual(input_page, int(skip_page), msg = '点击页面跳转失败，输入页面为%s，实际跳转页面为%s'%(input_page, skip_page))
		print('%s  结束物料页面输入跳转测试' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time()))))
	
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
	unittest.main()