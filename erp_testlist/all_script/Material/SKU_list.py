#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select 
from selenium.common.exceptions import NoSuchElementException
import sys, os, time, unittest, re
sys.path.append('..')
from public import *
reload(sys)
sys.setdefaultencoding('utf8')

class Sku_list(unittest.TestCase):
	'''SKU列表'''

	def setUp(self):
		#参数设置
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.login_url = linkaddress.link()
		self.verificationErrors = []
		self.accept_next_alert = True
		name = 'SKU列表'
		print_path.print_path(name)

	def test_add_skip(self):
		'''点击新增按钮跳转'''
		print('%s  开始新增按钮点击跳转测试' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time()))))
		driver = self.driver
		driver.get(login_url)
		login.login(driver)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/div').click()   #点击物料
		time.sleep(1)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/ul/li[1]/div').click()   #点击物料管理
		time.sleep(1)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/ul/li[1]/ul/li[2]').click()   #点击SKU列表
		time.sleep(1)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[2]/section/div/div[2]/section/div[2]/div/button').click()   #点击左上角新增按钮
		proving_info = '规格'    #使用新增页面的唯一存在的"规格"字段来验证
		print('%s 使用新增页面的唯一存在的"%s"字段来验证' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time())), proving_info))
		gain_info = location.findXpath(driver, '//*[@id="app"]/div/div[2]/div/div[2]/section/div/div[2]/div/form/div[2]/h3/text()').text   #定位跳转后的规格字段
		print('%s 定位到新增页面的"%s"字段' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time())), gain_info))
		self.assertEqual(proving_info, gain_info, msg = '点击物料列表左上角新增按钮跳转失败')
		print('%s  结束新增按钮点击跳转测试' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time()))))

	def test_sku_title_right(self):
		'''输入存在的sku标题筛选信息'''
		print('%s  开始输入存在的sku标题测试' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time()))))
		driver = self.driver
		driver.get(login_url)
		login.login(driver)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/div').click()   #点击物料
		time.sleep(1)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/ul/li[1]/div').click()   #点击物料管理
		time.sleep(1)
		location.findXpath(driver, '/html/body/div/div/div[2]/div/div[1]/aside/ul/li[1]/ul/li[1]/ul/li[2]').click()   #点击SKU列表
		time.sleep(1)
		location.findXpath(driver, '//*[@id="app"]/div/div[2]/div/div[2]/section/div/div[2]/section/div[1]/div[2]/form/div[1]/div[1]/div/div/div/input').clear()   #清空sku标题输入框内容
		search_content = location.findXpath(driver, '//*[@id="app"]/div/div[2]/div/div[2]/section/div/div[2]/section/div[3]/div[3]/table/tbody/tr[1]/td[1]/div').text   #获取列表下第一个sku标题
		print('%s 将使用获取到的第一项sku标题：%s进行筛选' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time())), search_content))
		location.findXpath(driver, '//*[@id="app"]/div/div[2]/div/div[2]/section/div/div[2]/section/div[1]/div[2]/form/div[1]/div[1]/div/div/div/input').send_keys(search_content)
		Obtain_content = location.findXpath(driver, '//*[@id="app"]/div/div[2]/div/div[2]/section/div/div[2]/section/div[3]/div[3]/table/tbody/tr[2]/td[1]/div').text   #获取到筛选结果的最后一项内容
		print('%s 将使用筛选后结果的最后一项内容：%s进行验证' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time())), Obtain_content))
		self.assertEqual(search_content, Obtain_content, msg = '输入存在的sku标题筛选的信息存在问题，筛选内容为：%s,实际获取内容为：%s' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time())), search_content, Obtain_content))
		print('%s  结束输入存在的sku标题测试' %(time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time()))))

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
	unittest.main()