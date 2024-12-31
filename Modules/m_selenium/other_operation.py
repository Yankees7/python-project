#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
主要操作: 选择元素 点击元素 输入字符串
其他操作: 可以通过Selenium提供的 ActionChains类 来实现
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# 创建wddriver实例对象
wd = webdriver.Edge()
wd.implicitly_wait(10)

# 打开指定网址
wd.get("https://www.baidu.com")

# 实例化
ac = ActionChains(wd)
# 鼠标移动到 元素上
ac.move_to_element(wd.find_element(By.CSS_SELECTOR, "[name='tj_briicon']")).perform()


# 调试不让关闭页面
input()
