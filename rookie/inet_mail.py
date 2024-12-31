from email.mime.text import MIMEText
from email.header import Header

import smtplib
import getpass

body = '''杨老师，你好
你好。
今天去峡谷吗
'''

# 'plain' 表示纯文本，'utf8'表示字符编码
message = MIMEText(body, 'plain', 'utf8')  # 设置正文本
message['From'] = Header('牛逼哄哄')  # 发件人
message['To'] = Header('yentrance@163.com')  # 收件人
message['Subject'] = Header('python互联网邮件测试')  # 主题

# dnwdakstlmctbhhi
smtp = smtplib.SMTP()  # 创建一个smtp对象
smtp.connect('smtp.qq.com')  # 连接邮件服务器
# smtp.starttls()  # 服务器要求安全登陆，需要则执行它，否则不需要
smtp.login('228357922@qq.com', 'dnwdakstlmctbhhi')  # 邮箱和授权码
smtp.sendmail('228357922@qq.com',
              ['yentrance@163.com', '228357922@qq.com','1079251659@qq.com'],
              message.as_bytes()
              )
