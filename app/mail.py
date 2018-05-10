import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '784797403@qq.com'  # 发件人邮箱账号
my_pass = 'hqfrzhydkyzybbab'  # 发件人邮箱密码(当时申请smtp给的口令)
my_user = '763858033@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail(title, select, content, email):
	my_sender = '784797403@qq.com'
	my_pass = 'hqfrzhydkyzybbab'
	ret = True
	try:
		msg = MIMEText(content, 'plain', 'utf-8')
		msg['From'] = formataddr(["求索管理员", my_sender])
		msg['To'] = formataddr(["就是你这个哔哔蛋", email])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
		msg['Subject'] = title+"-" + select  # 邮件的主题

		server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
		server.login(my_sender, my_pass)
		server.sendmail(my_sender, [email, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
		server.quit()  # 关闭连接
	except Exception:
		ret = False
	return ret

# ret=mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print("邮件发送失败")