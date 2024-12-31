import smtplib
import os
import imghdr
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# 设置邮件内容
msg = MIMEMultipart()
msg["Subject"] = "邮件主题"
msg["From"] = "发件人邮箱"
msg["To"] = "收件人邮箱"

# 添加 HTML 内容，包括嵌入图片
html_content = """
<html>
  <body>
    <p>这是一封带有 HTML 内容和嵌入图片的邮件。</p >
    <p>下面是嵌入的图片：</p >
    < img src="data:image/png;base64,{}" alt="embedded_image">
  </body>
</html>
"""
image_path = "图片路径"
with open(image_path, "rb") as img_file:
    image_data = img_file.read()
    image_type = imghdr.what(None, image_data)
    image_base64 = base64.b64encode(image_data).decode("utf-8")
    html_content = html_content.format(image_base64)

html_part = MIMEText(html_content, "html")
msg.attach(html_part)

# 添加附件
file_path = "文件路径"
with open(file_path, "rb") as file:
    attachment = MIMEApplication(file.read(), Name="文件名")
    attachment["Content-Disposition"] = f'attachment; filename="{os.path.basename(file_path)}"'
    msg.attach(attachment)

# 发送邮件
smtp_server = "SMTP 服务器地址"
smtp_port = 587  # SMTP 端口号
smtp_username = "你的邮箱用户名"
smtp_password = "你的邮箱密码"

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
