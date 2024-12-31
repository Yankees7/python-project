"""
示例二: 根据class属性,根据tag名选择元素
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建wddriver对象
wd = webdriver.Edge()

# 打开指定网址
wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")

# 根据class属性，选择元素
# 返回所有符合条件element列表对象,没有就是空列表
# 如果这里用find_element，只会找到符合条件的第一个，没有就异常
elements_lsit = wd.find_elements(By.CLASS_NAME, "animal")

# 取出列表中的每个element对象，打印出其text属性值
for element in elements_lsit:
    print(f"这里通过class:animal找到的元素.text: {element.text}")

# 根据tag名，选择元素，find_elements返回都是元素列表对象
elements_list_by_tag = wd.find_elements(By.TAG_NAME, "span")
# 取出列表中的每个wdelement对象，打印出其text属性值
for element in elements_list_by_tag:
    print(f"这里是通过tag:span找到的元素.text: {element.text}")

# 退出该网站
# wd.quit()

# 调试不让关闭页面
input()
