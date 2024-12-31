"""2.使用email.message来发送HTML内容(嵌入图片)"""

import os
import smtplib
import ssl
from email.message import EmailMessage  # 使用EmailMeaagae类，比直接使用fstring更容易编辑，邮件内容
from email.utils import make_msgid

"""2.使用email.message来发送HTML内容, 附件"""
EMAIL_ADDRESS = "yentrance@163.com"
EMAIL_PASSWORD = "DMNDXVPWCDSGOUMC"

context = ssl.create_default_context()  # 使用ssl对主机进校验

sender = EMAIL_ADDRESS
reciver = EMAIL_ADDRESS

"""邮件编辑"""
subject = "Python email subject"
body = "Hello,this is  an eamil sent by python!"
msg = EmailMessage()

msg["subject"] = subject
msg["From"] = EMAIL_ADDRESS
msg["To"] = [EMAIL_ADDRESS, "228357922@qq.com", "ayentrance@gmail.com"]
# 收件人多个：msg["To"] =

# 1.正文文本
msg.set_content(body)

# 2.添加附件（这里附件和html内容只能二选一发送）
# script_dir = os.path.dirname(os.path.abspath(__file__))
# filename = f"{script_dir}/OIP-C.jpg"
# with open(filename, "rb") as f:
#     filedata = f.read()
# msg.add_attachment(filedata, maintype="image", subtype="jpg", filename="OIP-C.jpg")

# 3.添加html正文(这里附件和html内容只能二选一发送）
# html
asparagus_cid = make_msgid()
html_context = """\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:Orange;">This is an HTML Email!</h1>
        <img src="cid:{asparagus_cid}" />
    </body>
</html>
""".format(
    asparagus_cid=asparagus_cid[1:-1]
)
msg.add_alternative(html_context, subtype="html")
# Now add the related image to the html part.
with open("roasted-asparagus.jpg", "rb") as img:
    msg.get_payload()[1].add_related(img.read(), "image", "jpeg", cid=asparagus_cid)
with open("outgoing.msg", "wb") as f:
    f.write(bytes(msg))

# Make a local copy of what we are going to send.
with open("outgoing.msg", "wb") as f:
    f.write(bytes(msg))
"""发送邮件"""
with smtplib.SMTP_SSL("smtp.163.com", 465, context=context) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
