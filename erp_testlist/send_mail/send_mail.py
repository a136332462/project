#coding:utf-8
import smtplib, os.path, mimetypes
import emial.MIMEMutipart, emial.MIMEText, email.MIMEBase

def send_mail(file_name):

	#构造MIMEMultipart对象作为根容器
	main_msg = email.MIMEMutipart.MIMEMutipart()

	#设置根容器属性
	From = "a136332462@126.com"
	To = '136332462@qq.com'
	main_msg['From'] = From
	main_msg['To'] = To
	main_msg['Subject'] = u'自动化测试报告'
	main_msg['Date'] = email.Utils.formatdate()
	server = smtplib.SMTP('smtp.126.com')
	server.login('a136332462@126.com', 'meilei99') #仅smtp服务器需要验证时

	#构造MIMEText对象作为邮件显示内容并附加到根容器
	#定义正文
	file = open(file_name, 'rb')
	main_body = file.read()
	text_msg = email.MIMEText.MIMEText(main_body, _subtype= 'html', 
		_charset= 'utf-8')

	#读入文件内容并格式化
	data = open(file_name, 'rb')
	ctype, encoding =  mimetypes.guess_type(file_name)
	if ctype is None or encoding is not None:
		ctype = 'application.octet-stream'
	maintype, subtype = ctype.split('/', 1)
	file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
	file_msg.set_payload(data.read())
	data.close()
	email.Encoders.encode_base64(file_msg) #将附件编码

	# 设置附件头  
	basename = os.path.basename(file_name)  
	file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头  
	main_msg.attach(file_msg)  
	  
	# 得到格式化后的完整文本  
	fullText = main_msg.as_string( )  
	  
	# 用smtp发送邮件  
	server.sendmail(From, To, fullText)