#coding:utf-8
import time,os 
import unittest
import HTMLTestRunner
from send_mail import send_mail
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#查找测试报告，调用发邮件的功能
def sendreport():
	result_dir = (os.getcwd() + '/all_script/test_data/result/')
	lists = os.listdir(result_dir)
	lists.sort(key = lambda fn: os.path.)