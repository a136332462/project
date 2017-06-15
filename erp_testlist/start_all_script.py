#coding:utf-8
import time, os, sys, time
import unittest
import  threading
import HTMLTestRunner
from send_mail import send_mail
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#查找测试报告，调用发邮件功能
def sendreport():
	new_files = []
	result_html = (os.getcwd() + '/all_script/data/html_result/')
	lists  = os.listdir(result_html)
	lists.sort(key = lambda fn: os.path.getmtime(result_html+ '/'+ fn )
		if not os.path.isdir(result_html+ '/'+ fn ) else 0)
	print(u'最新测试生成的报告:'+ lists[-1])

	#找到最新生成的文件
	new_file = os.path.join(result_html, lists[-1])
	new_files.append(new_file)

	result_dir = (os.getcwd() + '/all_script/data/text_result/')
	lists  = os.listdir(result_dir)
	lists.sort(key = lambda fn: os.path.getmtime(result_dir+ '/'+ fn )
		if not os.path.isdir(result_dir+ '/'+ fn ) else 0)
	print(u'最新测试生成的报告:'+ lists[-1])

	#找到最新生成的文件
	new_file = os.path.join(result_dir, lists[-1])
	new_files.append(new_file)
	print new_files
	
	#调用发邮件模块
	send_mail.send_mail(new_files)

#========================将测试用例添加到测试套件========================
def creatsuite():
	testunit = unittest.TestSuite()

	#定义测试文件查找目录
	test_dir = (os.getcwd()+ '/all_script/')

	#定义discover方法的参数
	discover = unittest.defaultTestLoader.discover(
		test_dir,
		pattern = 'start_*.py',
		top_level_dir = None)

	#discover方法筛选出来的用例，循环添加到测试套件中
	for test_case in discover:
		testunit.addTests(test_case)
	return testunit

now_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))
file_name = (os.getcwd() + '/all_script/data/html_result/')+ now_time + 'result.html'
fp = file(file_name, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
	stream = fp,
	title = '测试用例报告',
	description = u'用例执行情况')

def EEEEEmultiRunCase(suite,casedir):
	proclist=[]
	s=0
	for i in suite:
		runner = HTMLTestRunner.HTMLTestRunner(
			stream = fp,
			title = '测试用例报告',
			description = u'用例执行情况')
		proc =threading.Thread(target=runner.run(i),args=(i,))
		proclist.append(proc)
		s=s+1
	return proclist

if __name__ == '__main__':
	alltestnames = creatsuite()
	proclist = EEEEEmultiRunCase(alltestnames[0],alltestnames[1])
	for proc in proclist:
		proc.start()
	for proc in proclist:
		proc.join()
	fp.close()
	# sendreport()