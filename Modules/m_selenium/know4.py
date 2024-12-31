#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

"""
等待元素出现
"""

# 创建wddriver实例对象
wd = webdriver.Edge()
# 3.正确的内置的等待元素出现,那么后续的find_element和find_elements之类的方法都会调用此策略，10为等待最大时长
wd.implicitly_wait(10)

# 打开指定网址
wd.get("https://www.byhy.net/_files/stock1.html")

# 通过id寻找获得webelemnt对象
element = wd.find_element(By.ID, "kw")
element.send_keys("通讯")

element = wd.find_element(By.ID, "go")
element.click()

# 根据查询后的结果，找di为1的所有内容
# import time
# 1.等待元素出现：time.sleep(1)  # 给服务器响应时间,方才能正确执行下面语句;但万一等待的时间不够
first = wd.find_element(By.ID, "1")
print(first.text)

# 2.等待元素出现
# while True:
#     try:
#         first = wd.find_element(By.ID, "1")
#         print(first.text)
#         break
#     except NoSuchElementException:
#         time.sleep(1)  # 预防耗cpu


# 退出该网站
# wd.quit()

# 调试不让关闭页面
input()

# 补充：
# 获取元素的属性值
# element.get_attribute("class")

# 获取元素全部内容
# element.get_attribute("outerHTML")

# 获取元素内部
# element.get_attribute("innerHTML")

# 针对输入框，已经输入的内容
# element.get_attribute("value")

# 有时候，element.text没有展示界面上或者没有完全展示
# element.get_attribute("innerText")
# element.get_attribute("textContent")
