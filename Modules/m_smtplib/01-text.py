"""
如何发送邮件？
内置模块: smtplib,email
准备邮件: email
发送邮件: smtplib

邮件类型：
1.纯文本邮件
2.HTML邮件
"""

import ssl  # 实现ssl加密通信

# from email.mime.text import MIMEText
from email.message import EmailMessage  # 使用EmailMeaagae类，比直接使用fstring更容易编辑，邮件内容
import smtplib


"""1.使用smtplib发送纯文本文件"""
# from getpass import getpass  # 交互式不显示的输入用户和密码
EMAIL_ADDRESS = "yentrance@163.com"  # EMAIL_ADDRESS = getpass("Email:")
EMAIL_PASSWORD = "DMNDXVPWCDSGOUMC"  # EMAIL_PASSWORD = getpass("Password:")
recivers = ["ayentrance@gmail.com", "228357922@qq.com"]
# 使用ssl对主机进校验
context = ssl.create_default_context()

# 准备邮件
msg = EmailMessage()
subject = "Python email subject"
body = "这是一封python测试邮件"
msg["subject"] = subject  # 主题
msg["From"] = EMAIL_ADDRESS  # 发件人
msg["To"] = ",".join(recivers)  # 收件人;多人这里确实要字符串格式
msg.set_content(body)  # 邮件正文

# 使用with as就不用使用smtp.quit()了，with中语句执行完as对象自动关闭
# smtp是我创建的邮件服务对象
with smtplib.SMTP_SSL("smtp.163.com", 465, context=context) as smtpobj:
    smtpobj.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtpobj.send_message(msg)  # 或 smtp.sendmail(sender, recivers, msg)
