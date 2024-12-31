import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

# 创建邮件对象
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
    < img src="cid:image1">
  </body>
</html>
"""
html_part = MIMEText(html_content, "html")
msg.attach(html_part)

# 添加嵌入的图片
with open("图片路径", "rb") as img_file:
    img_data = img_file.read()
    img_part = MIMEImage(img_data)
    img_part.add_header("Content-ID", "<image1>")
    msg.attach(img_part)

# 添加附件
with open("附件路径", "rb") as file:
    attachment = MIMEApplication(file.read(), Name="文件名")
    attachment["Content-Disposition"] = f'attachment; filename="{attachment_filename}"'
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
