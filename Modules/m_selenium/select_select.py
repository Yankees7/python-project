#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
选择框分类: radio框、checkout框、select框
radio,checkbox框都是input元素，只是里面的type不同而已
select: select框则是一个新的select标签
对于select框，selenium专门提供了一个 Select类 进行操作
select类：提供select_by_value方法
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

"""radio"""
# 创建wddriver实例对象
wd = webdriver.Edge()
wd.implicitly_wait(10)

# 打开指定网址
wd.get("https://cdn2.byhy.net/files/selenium/test2.html")

"""单选框"""
from selenium.webdriver.support.ui import Select

# 创建Select对象
select = Select(wd.find_element(By.CSS_SELECTOR, "#ss_single"))
# 通过Select对象选中小雷老师--根据 可见文本
select.select_by_visible_text("小雷老师")

"""多选框"""
# 创建Select对象
select1 = Select(wd.find_element(By.CSS_SELECTOR, "#ss_multi"))
# 清除所有 已经选中 的选项
select1.deselect_all()
# 选择小雷老师 和 小凯老师
select1.select_by_visible_text("小雷老师")
select1.select_by_visible_text("小凯老师")


# 根据 value属性值 选择
# 根据 index 选择
# 根据 次序 选择
# 根据 可见文本 选择

# 调试不让关闭页面
input()
