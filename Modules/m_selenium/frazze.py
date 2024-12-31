"""鼠标悬停之后，动态显示的界面，进行冻结方便选取元素
1.F12开发者工具
2.点击console
3.输入: setTimeout(function(){debugger},5000) 延迟5s进行冻结界面
4.鼠标悬停至目标出（延迟是为了给鼠标悬停的操作时间）
5.等待冻结，然后界面就选到元素了，方便代码寻找element对象
"""

"""弹出对话框
分类：
1.Alert: 通知信息
模拟用户点击ok: driver.switch_to.alert.accpect()
获取弹出对话框的文本: driver.switch_to.alert.text
confirm: 需要确认操作，例如删除账号
prompt: 需输入一些信息提交上去
还有一些对话框就是html本身自带的内容，直接用以前的方法即可解决。
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Edge()
wd.implicitly_wait(5)
wd.get("https://cdn2.byhy.net/files/selenium/test4.html")

# ---Alert示例---
wd.find_element(By.ID, "b1").click()  # 点击这就会弹出对话框
# 打印弹出框 提示信息
print(wd.switch_to.alert.text)
# 点击ok按钮
wd.switch_to.alert.accept()

# ---confirm示例---
wd.find_element(By.ID, "b2").click()  # 弹出对话框
# 提示信息 和 ok 和上面代码一样
# 点击取消按钮
wd.switch_to.alert.dismiss()

# ---prompt示例---
wd.find_element(By.ID, "b3").click()  # 弹出对话框
# 提示信息 和 ok 取消 和上面代码一样
# 获取alert对象(这样只是方便而已)
alert = wd.switch_to.alert
# 打印弹出框信息
print(alert.text)
# 输入信息并ok
alert.send_keys("web自动化 - selenium")
alert.accept()


input()
