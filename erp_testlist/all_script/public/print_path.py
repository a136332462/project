#coding:utf-8
import os.path
import os
import sys, time

now_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
def print_path(name):
	f_result = open(os.getcwd() + '/all_script/data/text_result/'+ now_time+'result.txt', 'a')
	sys.stdout = f_result
	print('------------------"开始记录%s输出，记录时间%s"------------------'%(name, time.strftime("%Y-%m-%d:%H:%M:%S",time.localtime(time.time()))))