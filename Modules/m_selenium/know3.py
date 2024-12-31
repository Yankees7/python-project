#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By

"""
可以根据webelement对象继续寻找元素对象
WebDriver对象，选择元素的范围是整个web页面
WebElement对象，选择元素的范式是该元素的内部
"""

# 创建wddriver实例对象
wd = webdriver.Edge()

# 打开指定网址
wd.get("https://cdn2.byhy.net/files/selenium/sample1.html")

# 通过id寻找获得webelemnt对象
element = wd.find_element(By.ID, "container")

# 根据webelement对象(id为container元素内部)继续寻找
spans = element.find_elements(By.TAG_NAME, "span")
for span in spans:
    print(span.text)

# 退出该网站
# wd.quit()

# 调试不让关闭页面
input()
