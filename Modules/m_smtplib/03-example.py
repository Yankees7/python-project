"""
3.使用local debug server接受邮件进行debug
先在终端开启debugserver: python -m smtpd -c DebuggingServer -n localhost:1025

No Module Named smptd,该模块smtpd在3.12版本移除: aiosmtpd软件包是此模块的推荐替代品
pip install aiosmtpde
命令行用法: python3 -m aiosmtpd -n 端口为8025

"""

import smtplib
import ssl  # 实现ssl加密通信


EMAIL_ADDRESS = "yentrance@163.com"
EMAIL_PASSWORD = "DMNDXVPWCDSGOUMC"

context = ssl.create_default_context()  # 使用ssl对主机进校验
sender = EMAIL_ADDRESS
reciver = EMAIL_ADDRESS

subject = "Python email subject"
body = "Hello,this is  an eamil sent by python!"
msg = f"Subject: {subject}\n\n{body}"


with smtplib.SMTP("localhost", 8025) as smtp:
    smtp.sendmail(sender, reciver, msg)
