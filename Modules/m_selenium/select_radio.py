#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
选择框分类: radio框、checkout框、select框
radio框: 直接用WebElement的click方法，模拟用户点击就可以了
checkbox: 也是直接用WebElemet的click方法，模拟用户点击，需要注意的是：要先获取当前复选框的状态，如果已经勾选了，就不能再点击，否则反而会取消选择
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

"""radio"""
# 创建wddriver实例对象
wd = webdriver.Edge()
wd.implicitly_wait(10)

# 打开指定网址
wd.get("https://cdn2.byhy.net/files/selenium/test2.html")

# 获取当前选中的元素
element = wd.find_element(By.CSS_SELECTOR, "#s_radio input[checked='checked']")
print(f'当前选中的是：{element.get_attribute("value")}')

# 点选小雷老师
element1 = wd.find_element(By.CSS_SELECTOR, "#s_radio input[value='小雷老师']").click()
element1.click()

"""checkbox"""


# 调试不让关闭页面
input()
